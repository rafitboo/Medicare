from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app import db
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.user import User
from app.models.admin import Admin

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
            name = request.form.get('name')
            description = request.form.get('description')
            category_id = request.form.get('category_id')
            price = request.form.get('price')
            stock = request.form.get('stock')

            success, message = admin_user.add_medicine(name, description, category_id, price, stock)
            flash(message, 'success' if success else 'error')

        return redirect(url_for('admin.manage_medicines'))

    medicines = Medicine.query.order_by(Medicine.name.asc()).all()
    categories = Category.query.all()
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
        name = request.form.get('name')
        description = request.form.get('description')
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
@admin.route('/admin/manage_users')
def manage_users():
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

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
        name = request.form.get('name')
        email = request.form.get('email')
        role = request.form.get('role')
        address = request.form.get('address')
        phone = request.form.get('phone')

        admin_user = Admin.query.get(session['user_id'])
        if admin_user.edit_user(user_id, name, email, role, address, phone):
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