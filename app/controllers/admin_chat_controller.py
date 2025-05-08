from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from app import db
from app.models.user import User
from app.models.admin import Admin
from app.models.staff import Staff
from app.models.chat import Chat
from app.models.notification import Notification

admin_chat = Blueprint('admin_chat', __name__)

@admin_chat.route('/admin/messages')
def messages():
    if session.get('user_role') not in ['admin', 'staff']:
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))
    
    user = Admin.query.get(session['user_id']) if session.get('user_role') == 'admin' else Staff.query.get(session['user_id'])
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('auth.login_page'))
        
    conversations = Chat.get_customer_conversation_summary()
    customers = []
    
    for conv in conversations:
        customer = User.query.get(conv['customer_id'])
        if customer:
            customers.append({
                'id': customer.id,
                'name': customer.username,
                'latest_message': conv['latest_message'],
                'timestamp': conv['timestamp'],
                'unread': conv['unread_count'],
                'original_timestamp': conv['original_timestamp']
            })
    
    return render_template('chat/messages.html', customers=customers, role=session.get('user_role'))

@admin_chat.route('/admin/messages/<int:customer_id>', methods=['GET', 'POST'])
def customer_conversation(customer_id):
    if session.get('user_role') not in ['admin', 'staff']:
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))
    
    user = Admin.query.get(session['user_id']) if session.get('user_role') == 'admin' else Staff.query.get(session['user_id'])
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('auth.login_page'))
        
    customer = User.query.get(customer_id)
    if not customer:
        flash('Customer not found', 'error')
        return redirect(url_for('admin_chat.messages'))
    
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            success, msg = Chat.add_message(customer_id, message, is_from_customer=False)
            if not success:
                flash(msg, 'error')
        return redirect(url_for('admin_chat.customer_conversation', customer_id=customer_id))
    
    conversation = Chat.get_customer_conversation_with_timestamps(customer_id)
    return render_template('chat/conversation.html', conversation=conversation, customer=customer, role=session.get('user_role'))

@admin_chat.route('/admin/notifications')
def notifications():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))
    
    notifications = Notification.query.order_by(Notification.timestamp.desc()).all()
    return render_template('admin/notifications.html', notifications=notifications)

@admin_chat.route('/admin/notifications/<int:notification_id>/mark-read', methods=['POST'])
def mark_notification_read(notification_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login'))
    
    success = Notification.mark_as_read(notification_id)
    if success:
        flash('Notification marked as read', 'success')
    else:
        flash('Failed to mark notification as read', 'error')
    return redirect(url_for('admin_chat.notifications'))

@admin_chat.route('/admin/notifications/mark-all-read', methods=['POST'])
def mark_all_notifications_read():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login'))
    
    success = Notification.mark_all_as_read()
    if success:
        flash('All notifications marked as read', 'success')
    else:
        flash('Failed to mark all notifications as read', 'error')
    return redirect(url_for('admin_chat.notifications'))