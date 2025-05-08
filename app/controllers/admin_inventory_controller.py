from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app import db
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.admin import Admin

admin_inventory = Blueprint('admin_inventory', __name__)

@admin_inventory.route('/admin/manage_medicines', methods=['GET', 'POST'])
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

        return redirect(url_for('admin_inventory.manage_medicines'))

    medicines = Medicine.query.order_by(Medicine.name.asc()).all()
    categories = Category.query.order_by(Category.name.asc()).all()
    return render_template('admin/manage_medicines.html', medicines=medicines, categories=categories)

@admin_inventory.route('/admin/edit_medicine/<int:medicine_id>', methods=['GET', 'POST'])
def edit_medicine(medicine_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    medicine = Medicine.query.get(medicine_id)
    if not medicine:
        flash('Medicine not found', 'error')
        return redirect(url_for('admin_inventory.manage_medicines'))

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
            return redirect(url_for('admin_inventory.manage_medicines'))

    categories = Category.query.all()
    return render_template('admin/edit_medicine.html', medicine=medicine, categories=categories)

@admin_inventory.route('/admin/delete_medicine/<int:medicine_id>', methods=['POST'])
def delete_medicine(medicine_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    admin_user = Admin.query.get(session['user_id'])
    success, message = admin_user.delete_medicine(medicine_id)
    flash(message, 'success' if success else 'error')

    return redirect(url_for('admin_inventory.manage_medicines'))

@admin_inventory.route('/admin/manage_categories', methods=['GET', 'POST'])
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

        return redirect(url_for('admin_inventory.manage_categories'))

    categories = Category.query.order_by(Category.name.asc()).all()
    return render_template('admin/manage_categories.html', categories=categories)

@admin_inventory.route('/admin/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    category = Category.query.get(category_id)
    if not category:
        flash('Category not found', 'error')
        return redirect(url_for('admin_inventory.manage_categories'))

    if request.method == 'POST':
        name = request.form.get('name').title()
        description = request.form.get('description').capitalize()
        admin_user = Admin.query.get(session['user_id'])
        success, message = admin_user.update_category(category_id, name, description)
        flash(message, 'success' if success else 'error')

        if success:
            return redirect(url_for('admin_inventory.manage_categories'))

    return render_template('admin/edit_category.html', category=category)

@admin_inventory.route('/admin/delete_category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    if session.get('user_role') != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('auth.login_page'))

    admin_user = Admin.query.get(session['user_id'])
    success, message = admin_user.delete_category(category_id)
    flash(message, 'success' if success else 'error')

    return redirect(url_for('admin_inventory.manage_categories')) 