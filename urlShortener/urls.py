from django.urls import path, include
from .views import homePage, redirect_url_view

appname = "urlShortener"

urlpatterns = [
    path('', homePage, name='homepage'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]