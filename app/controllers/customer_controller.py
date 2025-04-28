from flask import Blueprint, flash, redirect, url_for, request, session, render_template, jsonify
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

def get_cart_data(user_id):
    if not user_id:
        return None, None, "Please login first"
    
    cart_items = Cart.get_cart_items(user_id)
    total = Cart.get_cart_total(user_id)
    return cart_items, total, None

@customer.route('/cart', methods=['GET'])
def get_cart():
    user_id = get_current_user_id()
    cart_items, total, error = get_cart_data(user_id)
    
    if error:
        flash(error, 'error')
        return redirect(url_for('auth.login_page'))
        
    return render_template('customer/mycart.html', cart_items=cart_items, total=total)

@customer.route('/cart/add', methods=['POST'])
def add_to_cart():
    user_id = get_current_user_id()
    if not user_id:
        flash('Please login first', 'error')
        return redirect(url_for('auth.login_page'))

    medicine_id = request.form.get('medicine_id')
    quantity = request.form.get('quantity', 1)

    cart_item, error = Cart.add_to_cart(user_id, medicine_id, int(quantity))
    if error:
        flash(error, 'error')
    else:
        flash('Item added to cart successfully!', 'success')
    return redirect(url_for('customer.dashboard'))

@customer.route('/cart/update/<int:medicine_id>', methods=['POST'])
def update_cart_item(medicine_id):
    user_id = session.get('user_id')
    if not user_id:
        flash('Please login first', 'error')
        return redirect(url_for('auth.login_page'))

    try:
        quantity = int(request.form.get('quantity', 1))
    except ValueError:
        flash('Invalid quantity', 'error')
        return redirect(url_for('customer.mycart'))


    medicine = Medicine.query.get(medicine_id)
    if not medicine:
        flash('Medicine not found', 'error')
        return redirect(url_for('customer.mycart'))

    if quantity > medicine.stock:
        flash(f'Only {medicine.stock} items available in stock!', 'error')
        return redirect(url_for('customer.mycart'))


    cart_item, error = Cart.update_cart_item(user_id, medicine_id, quantity)
    if error:
        flash(error, 'error')
    else:
        flash('Quantity updated successfully!', 'success')
    
    return redirect(url_for('customer.mycart'))

@customer.route('/cart/remove/<int:medicine_id>', methods=['POST'])
def remove_from_cart(medicine_id):
    user_id = get_current_user_id()
    if not user_id:
        flash('Please login first', 'error')
        return redirect(url_for('auth.login_page'))

    success, error = Cart.remove_from_cart(user_id, medicine_id)
    if error:
        flash(error, 'error')
    else:
        flash('Item removed from cart successfully!', 'success')
    return redirect(url_for('customer.mycart'))

@customer.route('/mycart', methods=['GET'])
def mycart():
    user_id = get_current_user_id()
    cart_items, total, error = get_cart_data(user_id)
    
    if error:
        flash(error, 'error')
        return redirect(url_for('auth.login_page'))
        
    return render_template('customer/mycart.html', cart_items=cart_items, total=total)

def get_current_user_id():
    return session.get('user_id')