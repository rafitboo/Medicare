from flask import Blueprint, flash, redirect, url_for, request, session, render_template
from app.models import db
from app.models.user import User
from app.models.cart import Cart
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.customer import Customer
from app.models.chat import Chat
from app.models.admin import Admin
from app.models.staff import Staff
from app.models.notification import Notification
from datetime import timedelta, datetime

staff = Blueprint('staff', __name__)

@staff.route('/staff/dashboard')
def dashboard():
    if session.get('user_role') != 'staff':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))
    return render_template('staff/dashboard.html')

@staff.route('/staff/messages')
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

@staff.route('/staff/messages/<int:customer_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('staff.messages'))
    
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            success, msg = Chat.add_message(customer_id, message, is_from_customer=False)
            if not success:
                flash(msg, 'error')
        return redirect(url_for('staff.customer_conversation', customer_id=customer_id))
    
    conversation = Chat.get_customer_conversation_with_timestamps(customer_id)
    return render_template('chat/conversation.html', conversation=conversation, customer=customer, role=session.get('user_role'))

@staff.route('/staff/notifications', methods=['GET', 'POST'])
def notifications():
    if session.get('user_role') != 'staff':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))
    
    staff_user = Staff.query.get(session['user_id'])
    
    if request.method == 'POST':
        message = request.form.get('message')
        notification_type = request.form.get('notification_type')
        
        if message and notification_type:
            success, msg = staff_user.notifyAdmin(message, notification_type)
            if success:
                flash('Notification sent successfully!', 'success')
            else:
                flash(msg, 'error')
            return redirect(url_for('staff.notifications'))
    
    # Get recent notifications sent by this staff member
    notifications = Notification.query.filter_by(staff_id=staff_user.id).order_by(Notification.timestamp.desc()).limit(10).all()
    
    return render_template('staff/notifications.html', notifications=notifications)