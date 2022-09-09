from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from subscriber import forms as CFORM
from urlShortener.models import ShortURLS
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

# statistics
@user_passes_test(lambda u: u.is_authenticated, login_url='login') 
def dashboard(request, pk):
	template = 'customer/dashboard.html'
	print('url=> ', request.get_host)
	context = {}
	all_urls = ShortURLS.objects.filter(user_id=pk)
	if request.user.is_superuser:
		all_urls = ShortURLS.objects.all()
		
	total_urls = all_urls.count()
	active_urls = all_urls.filter(is_deleted=False)
	deactive_urls = all_urls.filter(is_deleted=True)

	total_active_urls = active_urls.count()
	total_deactive_urls = deactive_urls.count()
	# print(total_url)
	context['total_urls'] = total_urls
	context['active_urls'] = active_urls
	context['deactive_urls'] = deactive_urls
	context['total_active_urls'] = total_active_urls
	context['total_deactive_urls'] = total_deactive_urls
	return render(request, template, context )