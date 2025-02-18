# myProject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Import redirect function
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
]
