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
from datetime import timedelta

customer = Blueprint('customer', __name__)

@customer.route('/dashboard')
def dashboard():
    medicines = Medicine.query.order_by(Medicine.name.asc()).all()
    categories = Category.query.all()  
    return render_template('customer/dashboard.html', medicines=medicines, categories=categories)

@customer.route('/cart', methods=['GET'])
def get_cart():
    user_id = get_current_user_id()
    if not user_id:
        flash('Please login first', 'error')
        return redirect(url_for('auth.login_page'))
    customer = Customer.query.get(user_id)
    if not customer:
        flash('Customer not found', 'error')
        return redirect(url_for('auth.login_page'))
    cart_items, total, error = customer.get_cart_data()
    
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
    customer = Customer.query.get(user_id)
    if not customer:
        flash('Customer not found', 'error')
        return redirect(url_for('auth.login_page'))
    medicine_id = request.form.get('medicine_id')
    quantity = request.form.get('quantity', 1)
    cart_item, error = customer.add_to_cart(medicine_id, int(quantity))
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
    customer = Customer.query.get(user_id)
    if not customer:
        flash('Customer not found', 'error')
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
    cart_item, error = customer.update_cart_item(medicine_id, quantity)
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
    customer = Customer.query.get(user_id)
    if not customer:
        flash('Customer not found', 'error')
        return redirect(url_for('auth.login_page'))
    success, error = customer.remove_from_cart(medicine_id)
    if error:
        flash(error, 'error')
    else:
        flash('Item removed from cart successfully!', 'success')
    return redirect(url_for('customer.mycart'))

@customer.route('/mycart', methods=['GET'])
def mycart():
    user_id = get_current_user_id()
    customer = Customer.query.get(user_id) if user_id else None
    if not customer:
        flash('Please login first', 'error')
        return redirect(url_for('auth.login_page'))
    cart_items, total, error = customer.get_cart_data()
    if error:
        flash(error, 'error')
        return redirect(url_for('auth.login_page'))
    return render_template('customer/mycart.html', cart_items=cart_items, total=total)

@customer.route('/messages', methods=['GET', 'POST'])
def customer_messages():
    user_id = get_current_user_id()
    if not user_id:
        flash('Please login first', 'error')
        return redirect(url_for('auth.login_page'))
    customer = Customer.query.get(user_id)
    if not customer:
        flash('Customer not found', 'error')
        return redirect(url_for('auth.login_page'))

    if request.method == 'POST':
        message = request.form.get('message')
        if message:

            Chat.add_message(customer_id=user_id, message=message, is_from_customer=True)
        return redirect(url_for('customer.customer_messages'))
    conversation = Chat.get_conversation(user_id)
    for msg in conversation:
        msg.bd_timestamp = msg.timestamp + timedelta(hours=6)
    return render_template('customer/customer_conversation.html', conversation=conversation, customer=customer)

def get_current_user_id():
    return session.get('user_id')