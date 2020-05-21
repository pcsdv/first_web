
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

from action.forms import UserLoginForm, UserRegisterForm



def logout_view(request):
	if request.method == 'POST':
		loguot(request)
		return redirect('accountslogin')
	


def index(request):
	return render(request,'action/index.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			login(request,user)
			return redirect('index')
	else:
		form = UserCreationForm()

	context = { 'form': form }
	return render(request,'registration/register.html',context)

