from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from app import db
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.user import User
from app.models.admin import Admin
from app.models.staff import Staff

admin_user = Blueprint('admin_user', __name__)

@admin_user.route('/admin/dashboard')
def dashboard():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    users = User.query.all()
    medicines = Medicine.query.all()
    categories = Category.query.all()
    return render_template('admin/dashboard.html', users=users, medicines=medicines, categories=categories)

@admin_user.route('/admin/manage_users', methods=['GET', 'POST'])
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
                return redirect(url_for('admin_user.manage_users'))

            success, message = admin_user.add_user(username, email, phone, role, address, password)
            flash(message, 'success' if success else 'error')

        return redirect(url_for('admin_user.manage_users'))

    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)

@admin_user.route('/admin/edit_users/<int:user_id>', methods=['GET', 'POST'])
def edit_users(user_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('admin_user.manage_users'))

    if request.method == 'POST':
        username = request.form.get('name').title()
        email = request.form.get('email').lower()
        role = request.form.get('role')
        address = request.form.get('address').title()
        phone = request.form.get('phone')

        admin_user = Admin.query.get(session['user_id'])
        if admin_user.edit_user(user_id, username, email, role, address, phone):
            flash('User updated successfully.', 'success')
            return redirect(url_for('admin_user.manage_users'))
        else:
            flash('Failed to update user.', 'error')

    return render_template('admin/edit_users.html', user=user)

@admin_user.route('/admin/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    admin_user = Admin.query.get(session['user_id'])
    if admin_user.delete_user(user_id):
        flash('User deleted successfully.', 'success')
    else:
        flash('Failed to delete user.', 'error')

    return redirect(url_for('admin_user.manage_users')) 