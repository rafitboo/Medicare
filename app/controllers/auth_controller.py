from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.user import User
from app.models.customer import Customer

auth = Blueprint('auth', __name__)
customer = Blueprint('customer', __name__)
staff = Blueprint('staff', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'GET':
        return render_template('auth/signup.html')

    username = request.form.get('username', '').title().strip()
    email = request.form.get('email', '').strip().lower()
    phone = request.form.get('phone', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '') 
    terms = request.form.get('terms')

    if not all([username, email, phone, password, confirm_password]):
        flash('All fields are required', 'error')
        return redirect(url_for('auth.signup_page'))

    if not terms:
        flash('You must agree to the terms', 'error')
        return redirect(url_for('auth.signup_page'))

    if password != confirm_password:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('auth.signup_page'))

    if len(password) < 8:
        flash('Password must be at least 8 characters', 'error')
        return redirect(url_for('auth.signup_page'))

    try:
        new_user, error = User.register(username, email, phone, password)
        if error:
            flash(error, 'error')
            return redirect(url_for('auth.signup_page'))

        flash('Account created! Please login', 'success')
        return redirect(url_for('auth.login_page'))

    except Exception as e:
        db.session.rollback()
        flash('Account creation failed', 'error')
        return redirect(url_for('auth.signup_page'))

@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '').strip()

    if not email or not password:
        flash('Email and password are required', 'error')
        return redirect(url_for('auth.login_page'))

    user = User.login(email, password)
    if not user:
        flash('Invalid email or password', 'error')
        return redirect(url_for('auth.login_page'))

    session['user_id'] = user.id
    session['user_role'] = user.role

    flash('Login successful!', 'success')
    if user.role == 'customer':
        return redirect(url_for('customer.dashboard'))
    elif user.role == 'admin':
        return redirect(url_for('admin.dashboard'))
    elif user.role == 'staff':
        return redirect(url_for('staff.dashboard'))
    else:
        flash('Invalid user role', 'error')
        return redirect(url_for('auth.login_page'))

@auth.route('/logout')
def logout():
    User.logout(session)
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login_page'))

# @customer.route('/dashboard')
# def dashboard():
#     medicines = Medicine.query.order_by(Medicine.name.asc()).all()
#     categories = Category.query.all()  
#     return render_template('customer/dashboard.html', medicines=medicines, categories=categories)

@staff.route('/staff/dashboard')
def dashboard():
    return render_template('staff/dashboard.html')