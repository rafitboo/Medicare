from flask import Blueprint, flash, redirect, url_for, request, session, render_template
from app.models import db
from app.models.user import User
from app.models.cart import Cart
from app.models.medicine import Medicine
from app.models.category import Category

customer = Blueprint('customer', __name__)

@customer.route('/dashboard')
def dashboard():
    medicines = Medicine.query.order_by(Medicine.name.asc()).all()
    categories = Category.query.all()  
    return render_template('customer/dashboard.html', medicines=medicines, categories=categories)

@customer.route('/cart', methods=['GET'])
def get_cart():
    user_id = get_current_user_id()
    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('auth.login_page'))

    cart_items = Cart.get_cart_items(user_id)
    return render_template('customer/mycart.html', cart_items=cart_items)

@customer.route('/cart/add', methods=['POST'])
def add_to_cart():
    user_id = get_current_user_id()
    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('auth.login_page'))

    data = request.get_json()
    medicine_id = data.get('medicine_id')
    quantity = data.get('quantity', 1)

    cart_item, error = Cart.add_to_cart(user_id, medicine_id, quantity)
    if error:
        flash(error, 'error')
    else:
        flash('Item added to cart successfully!', 'success')

    return redirect(url_for('customer.get_cart'))

@customer.route('/cart/remove/<int:medicine_id>', methods=['DELETE'])
def remove_from_cart(medicine_id):
    user_id = get_current_user_id()
    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('auth.login_page'))

    success, error = Cart.remove_from_cart(user_id, medicine_id)
    if error:
        flash(error, 'error')
    else:
        flash('Item removed from cart successfully!', 'success')

    return redirect(url_for('customer.get_cart'))

@customer.route('/mycart', methods=['GET'])
def mycart():
    user_id = get_current_user_id()
    user = User.query.get(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('auth.login_page'))

    cart_items = Cart.get_cart_items(user_id)
    return render_template('customer/mycart.html', cart_items=cart_items)

# Helper function to get current user ID
def get_current_user_id():
    return session.get('user_id')