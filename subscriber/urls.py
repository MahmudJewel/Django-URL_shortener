from django.urls import path, include
from .views import customerSignup
from django.contrib.auth.views import LoginView, LogoutView

appname = "subscriber"

urlpatterns = [
    path('signup', customerSignup, name='customerSignup'),
    path('login', LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='customer/logout.html'), name='logout'),
]