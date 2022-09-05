from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from subscriber import forms as CFORM
# Create your views here.

def customerSignup(request):
	RegisterForm = CFORM.RegisterForm()
	if request.method == 'POST':
		RegisterForm = CFORM.RegisterForm(request.POST)
		if RegisterForm.is_valid():
			customer=RegisterForm.save()
			customer_group=Group.objects.get_or_create(name='CUSTOMER')
			customer_group[0].user_set.add(customer)
			username=RegisterForm.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}")
			return redirect('login')
		#return redirect('login')
			
	context={
		'RegisterForm': RegisterForm,
	}
	return render(request, 'customer/signup.html',context)
