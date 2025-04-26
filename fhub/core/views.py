from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_views(request):
    return render(request, 'home.html')

def land_view(request):
    return render(request, 'landing.html')

@csrf_protect
def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login') 
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error(None, 'Invalid email or password.')
            except User.DoesNotExist:
                form.add_error('email', 'No account found with this email.')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


#expenses part
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense, Budget
from .forms import ExpenseForm, BudgetForm
from django.db.models import Sum
from datetime import date
from datetime import datetime, date
import calendar

@login_required
def expense_dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    current_year = date.today().year
    current_month = date.today().month

    if start_date:
        expenses = expenses.filter(date__gte=start_date)
        filter_date = datetime.strptime(start_date, "%Y-%m-%d")
        filter_year = filter_date.year
        filter_month = filter_date.month
    else:
        filter_year = date.today().year
        filter_month = current_month
    if end_date:
        expenses = expenses.filter(date__lte=end_date)

    

    budget = Budget.objects.filter(user=request.user, year=filter_year, month=filter_month).first()
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = budget.amount - total_expenses if budget else 0

    category_summary = expenses.values('category').annotate(total=Sum('amount')).order_by('category')

    month_labels = [calendar.month_name[i] for i in range(1, 13)]
    month_totals = [
        Expense.objects.filter(user=request.user, date__year=current_year, date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0
        for month in range(1, 13)
    ]

    if request.method == 'POST':
        if 'add_expense' in request.POST:
            expense_form = ExpenseForm(request.POST)
            budget_form = BudgetForm()
            if expense_form.is_valid():
                new_expense = expense_form.save(commit=False)
                new_expense.user = request.user
                new_expense.save()
                return redirect('expense-dashboard')
        elif 'set_budget' in request.POST:
            budget_form = BudgetForm(request.POST)
            expense_form = ExpenseForm()
            if budget_form.is_valid():
                Budget.objects.update_or_create(
                    user=request.user,
                    year=budget_form.cleaned_data['year'],
                    month=budget_form.cleaned_data['month'],
                    defaults={'amount': budget_form.cleaned_data['amount']}
                )
                return redirect('expense-dashboard')
    else:
        expense_form = ExpenseForm()
        budget_form = BudgetForm()

    context = {
        'expenses': expenses,
        'budget': budget.amount if budget else 0,
        'total_expenses': total_expenses,
        'balance': balance,
        'expense_form': expense_form,
        'budget_form': budget_form,
        'category_summary': category_summary,
        'month_labels': month_labels,
        'month_totals': month_totals,
        'start_date': start_date,
        'end_date': end_date, 
    }
    return render(request, 'expenses.html', context)


@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect('expense-dashboard')
