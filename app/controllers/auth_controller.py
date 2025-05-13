from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db
from app.models.medicine import Medicine
from app.models.category import Category
from app.models.user import User
from app.models.customer import Customer
from functools import wraps

auth = Blueprint('auth', __name__)
customer = Blueprint('customer', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

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

    user, error = User.signup(username, email, phone, password, confirm_password, terms)
    if error:
        flash(error, 'error')
        return redirect(url_for('auth.signup_page'))

    flash('Account created! Please login', 'success')
    return redirect(url_for('auth.login_page'))

@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '').strip()

    user, error = User.login(email, password)
    if error:
        flash(error, 'error')
        return redirect(url_for('auth.login_page'))

    session['user_id'] = user.id
    session['user_role'] = user.role

    flash('Login successful!', 'success')
    if user.role == 'customer':
        return redirect(url_for('customer.dashboard'))
    elif user.role == 'admin':
        return redirect(url_for('admin_user.dashboard'))
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

@auth.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'GET':
        user = User.query.get(session['user_id'])
        if not user:
            flash('User not found', 'error')
            return redirect(url_for('auth.login'))
        return render_template('profile/edit_profile.html', user=user)
    
    if request.method == 'POST':
        user = User.query.get(session['user_id'])
        if not user:
            flash('User not found', 'error')
            return redirect(url_for('auth.login'))
        
        # Verify current password
        if not user.check_password(request.form.get('current_password')):
            flash('Current password is incorrect', 'error')
            return redirect(url_for('auth.edit_profile'))
        
        # Prepare update data
        update_data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'address': request.form.get('address')
        }
        
        # Handle password change if new password is provided
        new_password = request.form.get('new_password')
        if new_password:
            if new_password != request.form.get('confirm_password'):
                flash('New passwords do not match', 'error')
                return redirect(url_for('auth.edit_profile'))
            update_data['password'] = new_password
        
        # Update profile
        success, message = user.update_profile(**update_data)
        if success:
            flash('Profile updated successfully', 'success')
            # Redirect based on user role
            if user.role == 'admin':
                return redirect(url_for('admin_user.dashboard'))
            elif user.role == 'staff':
                return redirect(url_for('staff.dashboard'))
            else:
                return redirect(url_for('customer.dashboard'))
        else:
            flash(message, 'error')
            return redirect(url_for('auth.edit_profile'))
