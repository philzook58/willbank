from django.shortcuts import render
from django.shortcuts import redirect,  get_object_or_404
from .models import Account
from django.contrib.auth.decorators import login_required





def index(request):
	return render(request, 'account/index.html', )

@login_required
def account_details(request,username):
	account = get_object_or_404(Account, user__username=username)
	return render(request, 'account/account.html', {'account':account})
	

# Create your views here.
