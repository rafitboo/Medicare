from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app import db
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.user import User
from app.models.admin import Admin
from app.models.staff import Staff
from app.models.chat import Chat
from datetime import timedelta, datetime

admin = Blueprint('admin', __name__)

@admin.route('/admin/dashboard')
def dashboard():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    users = User.query.all()
    medicines = Medicine.query.all()
    categories = Category.query.all()
    return render_template('admin/dashboard.html', users=users, medicines=medicines, categories=categories)

@admin.route('/admin/manage_medicines', methods=['GET', 'POST'])
def manage_medicines():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    if request.method == 'POST':
        action = request.form.get('action')
        admin_user = Admin.query.get(session['user_id'])

        if action == 'add':
            name = request.form.get('name').title()
            description = request.form.get('description')
            category_id = request.form.get('category_id').capitalize()
            price = request.form.get('price')
            stock = request.form.get('stock')

            success, message = admin_user.add_medicine(name, description, category_id, price, stock)
            flash(message, 'success' if success else 'error')

        return redirect(url_for('admin.manage_medicines'))

    medicines = Medicine.query.order_by(Medicine.name.asc()).all()
    categories = Category.query.order_by(Category.name.asc()).all()
    return render_template('admin/manage_medicines.html', medicines=medicines, categories=categories)


@admin.route('/admin/edit_medicine/<int:medicine_id>', methods=['GET', 'POST'])
def edit_medicine(medicine_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    medicine = Medicine.query.get(medicine_id)
    if not medicine:
        flash('Medicine not found', 'error')
        return redirect(url_for('admin.manage_medicines'))

    if request.method == 'POST':
        name = request.form.get('name').title()
        description = request.form.get('description').capitalize()
        category_id = request.form.get('category_id')
        price = request.form.get('price')
        stock = request.form.get('stock')

        admin_user = Admin.query.get(session['user_id'])
        success, message = admin_user.update_medicine(medicine_id, name, description, category_id, price, stock)
        flash(message, 'success' if success else 'error')

        if success:
            return redirect(url_for('admin.manage_medicines'))

    categories = Category.query.all()
    return render_template('admin/edit_medicine.html', medicine=medicine, categories=categories)


@admin.route('/admin/delete_medicine/<int:medicine_id>', methods=['POST'])
def delete_medicine(medicine_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    admin_user = Admin.query.get(session['user_id'])
    success, message = admin_user.delete_medicine(medicine_id)
    flash(message, 'success' if success else 'error')

    return redirect(url_for('admin.manage_medicines'))

@admin.route('/admin/manage_users', methods=['GET', 'POST'])
def manage_users():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    if request.method == 'POST':
        action = request.form.get('action')
        admin_user = Admin.query.get(session['user_id'])

        if action == 'add':
            username = request.form.get('username').title()
            email = request.form.get('email').lower()
            phone = request.form.get('phone')
            role = request.form.get('role')
            address = request.form.get('address').title()
            password = request.form.get('password')

            if not username or not email or not password:
                flash("Username, email, and password are required.", "error")
                return redirect(url_for('admin.manage_users'))

            success, message = admin_user.add_user(username, email, phone, role, address, password)
            flash(message, 'success' if success else 'error')

        return redirect(url_for('admin.manage_users'))

    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)


@admin.route('/admin/edit_users/<int:user_id>', methods=['GET', 'POST'])
def edit_users(user_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('admin.manage_users'))

    if request.method == 'POST':
        username = request.form.get('name').title()
        email = request.form.get('email').lower()
        role = request.form.get('role')
        address = request.form.get('address').title()
        phone = request.form.get('phone')

        admin_user = Admin.query.get(session['user_id'])
        if admin_user.edit_user(user_id, username, email, role, address, phone):
            flash('User updated successfully.', 'success')
            return redirect(url_for('admin.manage_users'))
        else:
            flash('Failed to update user.', 'error')

    return render_template('admin/edit_users.html', user=user)

@admin.route('/admin/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    admin_user = Admin.query.get(session['user_id'])
    if admin_user.delete_user(user_id):
        flash('User deleted successfully.', 'success')
    else:
        flash('Failed to delete user.', 'error')

    return redirect(url_for('admin.manage_users'))

@admin.route('/admin/manage_categories', methods=['GET', 'POST'])
def manage_categories():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    if request.method == 'POST':
        action = request.form.get('action')
        admin_user = Admin.query.get(session['user_id'])

        if action == 'add':
            name = request.form.get('name').title()
            description = request.form.get('description').capitalize()
            success, message = admin_user.add_category(name, description)
            flash(message, 'success' if success else 'error')

        return redirect(url_for('admin.manage_categories'))

    categories = Category.query.order_by(Category.name.asc()).all()
    return render_template('admin/manage_categories.html', categories=categories)


@admin.route('/admin/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    category = Category.query.get(category_id)
    if not category:
        flash('Category not found', 'error')
        return redirect(url_for('admin.manage_categories'))

    if request.method == 'POST':
        name = request.form.get('name').title()
        description = request.form.get('description').capitalize()
        admin_user = Admin.query.get(session['user_id'])
        success, message = admin_user.update_category(category_id, name, description)
        flash(message, 'success' if success else 'error')

        if success:
            return redirect(url_for('admin.manage_categories'))

    return render_template('admin/edit_category.html', category=category)


@admin.route('/admin/delete_category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    admin_user = Admin.query.get(session['user_id'])
    success, message = admin_user.delete_category(category_id)
    flash(message, 'success' if success else 'error')

    return redirect(url_for('admin.manage_categories'))

@admin.route('/admin/messages')
def messages():
    if session.get('user_role') not in ['admin', 'staff']:
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))
    
    admin_user = Admin.query.get(session['user_id']) if session.get('user_role') == 'admin' else Staff.query.get(session['user_id'])
    customer_ids = admin_user.get_all_customer_conversations()
    customers = []
    
    for cust_id in customer_ids:
        customer = User.query.get(cust_id)
        if customer:
            latest_message = Chat.query.filter_by(customer_id=cust_id).order_by(Chat.timestamp.desc()).first()
            unread_count = Chat.query.filter_by(customer_id=cust_id, is_read=False, is_from_customer=True).count()

            bd_timestamp = latest_message.timestamp + timedelta(hours=6) if latest_message else None
            
            customers.append({
                'id': customer.id,
                'name': customer.username,
                'latest_message': latest_message.message if latest_message else 'No messages',
                'timestamp': bd_timestamp,
                'unread': unread_count,
                'original_timestamp': latest_message.timestamp if latest_message else None  # Store original timestamp for sorting
            })
    

    customers = sorted(customers, key=lambda x: x['original_timestamp'] or datetime.min, reverse=True)
    
    return render_template('admin/messages.html', customers=customers)

@admin.route('/admin/messages/<int:customer_id>', methods=['GET', 'POST'])
def customer_conversation(customer_id):
    if session.get('user_role') not in ['admin', 'staff']:
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))
    
    admin_user = Admin.query.get(session['user_id']) if session.get('user_role') == 'admin' else Staff.query.get(session['user_id'])
    customer = User.query.get(customer_id)
    
    if not customer:
        flash('Customer not found', 'error')
        return redirect(url_for('admin.messages'))
    
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            success, msg = admin_user.respondToChat(customer_id, message)
            if not success:
                flash(msg, 'error')
        return redirect(url_for('admin.customer_conversation', customer_id=customer_id))
    
    conversation = admin_user.get_customer_conversation(customer_id)
    for msg in conversation:
        msg.bd_timestamp = msg.timestamp + timedelta(hours=6)

    return render_template('admin/conversation.html', conversation=conversation, customer=customer)