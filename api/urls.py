from django.urls import path, include
from .views import AllUrls, CreateUrls

appname = "api"

urlpatterns = [
    # auth url 
    path('auth/', include('rest_framework.urls')),

    # create short link 
    path('create/', CreateUrls.as_view(), name='create'),
    path('list/', AllUrls.as_view(), name='all'),
]