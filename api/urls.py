from django.urls import path, include
from .views import ShortUrl_class

appname = "api"

urlpatterns = [
    # auth url 
    path('auth/', include('rest_framework.urls')),

    # create short link 
    path('create/', ShortUrl_class.as_view(), name='create')
]