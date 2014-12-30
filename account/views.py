from django.shortcuts import render
from django.shortcuts import redirect,  get_object_or_404
from .models import Account
from .forms import TransactionForm, UserForm
from django.contrib.auth.decorators import login_required





def index(request):
	return render(request, 'account/index.html', )

@login_required
def account_details(request,username):
	account = get_object_or_404(Account, user__username=username)
	return render(request, 'account/account.html', {'account':account})

@login_required
def profile(request):
	#account = get_object_or_404(Account, user__username=username)
	return render(request, 'account/profile.html', )#{'account':account})

def add_transaction(request):
	if request.method =='POST':
		form = TransactionForm(request.POST)
	else:
		form = TransactionForm()
	return render(request, 'account/add_transaction.html', {'form':form})

def register(request):
	if request.method =='POST':
		form = UserForm(request.POST)
	else:
		form = UserForm()
	return render(request, 'registration/register.html',{'form':form} )
	
	

# Create your views here.
