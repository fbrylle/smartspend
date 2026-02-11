from flask import Blueprint, redirect, render_template, flash, url_for, request, abort
from flask_login import login_required, login_user, logout_user, current_user
from .actions import create_new_user, authenticate_user, create_new_category, get_category_data, get_category_data_by_name, create_new_expense, get_expense_data, get_total_expenses, get_daily_expense, get_monthly_expense, edit_category_name, edit_expense_service, get_category_data_by_id, get_expense_data_by_id
from .schemas import LoginSchema, RegistrationSchema, CategorySchema, ExpenseSchema
from pydantic import ValidationError
from app.models import Category, Expense

main_app = Blueprint('main', __name__)


@main_app.route('/')
def index():
    return render_template('home.html')


@main_app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            valid_data = LoginSchema(**data) 
            attempted_user = authenticate_user(valid_data)

            if attempted_user and attempted_user.check_password(valid_data.password.get_secret_value()):
                login_user(attempted_user)
                flash(f'Welcome {attempted_user.fname}', 'success')
                return redirect(url_for('main.dashboard'))
            else:
                flash('Invalid username or password', 'danger')

        except ValidationError as e:
            flash('Check your inputs.', "warning")
    return render_template('login.html')


@main_app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    try:
        if request.method == "POST":
            data = request.form.to_dict()
            valid_data = RegistrationSchema(**data)

            if valid_data:
                create_new_user(valid_data)
                flash('User has been created', 'success')
                return redirect(url_for('main.login'))
    except ValidationError as e:
        error = e.errors()[0]['msg']
        flash(f"{error}", 'danger')
    return render_template('signup.html')


@main_app.route('/features')
def features():
    return render_template('features.html')


@main_app.route('/contact')
def contact():
    return render_template('contact.html')


# ----------protected routes---------------


@main_app.route('/dashboard')
@login_required
def dashboard():
    categories = get_category_data(current_user)
    total_spent = get_total_expenses(current_user)
    daily_spent = get_daily_expense(current_user)
    monthly_spent = get_monthly_expense(current_user)
    return render_template('dashboard.html', categories=categories, total_spent=total_spent, daily_spent=daily_spent, monthly_spent=monthly_spent)


@main_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main_app.route('/dashboard/add-category', methods=['GET', 'POST'])
@login_required
def add_category():

    if request.method == "POST":
        success, message = create_new_category(current_user, request.form.to_dict())
        flash(message, 'success' if success else 'danger')
        return redirect(url_for('main.dashboard'))

    return render_template('add-category.html')


@main_app.route('/dashboard/<id>')
@login_required
def expense(id):
    
    category = get_category_data_by_id(id, current_user)
    expenses = get_expense_data()

    return render_template('expenses.html', category=category, expenses=expenses)


@main_app.route('/dashboard/<id>/add-expense', methods=['GET', 'POST'])
@login_required
def add_expense(id):

    category = get_category_data_by_id(id, current_user)
    
    if request.method == "POST":
        success, message = create_new_expense(current_user, category.id, request.form.to_dict())
        flash(message, 'success' if success else 'danger')
        return redirect(url_for('main.expense', id=category.id))
    return render_template('add-expense.html', category=category)


@main_app.route('/dashboard/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_category(id):   
    
    if request.method == "GET":
        category = get_category_data_by_id(id, current_user)
        if category:
            return render_template('edit-category.html', category=category)
        else:
            abort(403)
            
    if request.method == "POST":
        success, message = edit_category_name(id, current_user.id, request.form.to_dict())
        flash(message, 'success' if success else 'danger')
        return redirect(url_for('main.dashboard'))
    

@main_app.route('/dashboard/edit/<category_id>/<expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(category_id, expense_id):

    category = get_category_data_by_id(category_id, current_user)
    expense = get_expense_data_by_id(expense_id, current_user.id)
    
    if request.method == "GET":
        expense = Expense.query.filter_by(id=expense_id, category_id=category_id, user_id=current_user.id).first()
        if expense:
            return render_template('edit-expense.html', expense=expense, category=category)
        else:
            abort(403)

    if request.method == "POST":
        success, message = edit_expense_service(category_id, expense_id, current_user.id, request.form.to_dict())
        flash(message, 'success' if success else 'danger')
        return redirect(url_for('main.expense', id=category.id))
    