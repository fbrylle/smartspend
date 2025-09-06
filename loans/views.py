from django.shortcuts import render, redirect
from .models import Loan, Payment, User
from .forms import LoanForm, PaymentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loans(request):
    if request.user.is_authenticated:
        loans = Loan.objects.filter(user=request.user)
    else:
        loans = None
    context = {'loans':loans}
    return render (request, 'loans/loans.html', context)


def loan(request, pk):
    loan = Loan.objects.get(id=pk)
    payments = Payment.objects.all()
    context = {'loan':loan, 'payments':payments}
    return render(request, 'loans/single-loan.html', context)

@login_required
def addLoan(request):
    form = LoanForm()
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loans')
    context = {'form':form}
    return render(request, 'loans/loans_form.html', context)

@login_required
def updateLoan(request, pk):
    loan = Loan.objects.get(id=pk)
    form = LoanForm(instance=loan)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('loans')
    context = {'loan':loan, 'form':form}
    return render(request, 'loans/loans_form.html', context)

@login_required
def deleteLoan(request, pk):
    loan = Loan.objects.get(id=pk)
    if request.method == 'POST':
        loan.delete()
        return redirect('loans')
    context = {'object':loan}
    return render(request, 'loans/delete_template.html', context)

@login_required
def addPayment(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('loans')
    else:
        form = PaymentForm(user=request.user)
    context = {'form':form}
    return render(request, 'loans/payments_form.html', context)


def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('loans')
        else:
            print('We encountered an error!')
    context = {'form':form}
    return render(request, 'loans/register.html', context)

def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('loans')
        else:
            print('Incorrect username or password.')

    return render(request, 'loans/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')