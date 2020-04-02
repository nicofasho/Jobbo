"""
Definition of urls for Blog_Scraper_Site.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('scrapes/<int:pk>', views.ScrapeDetail.as_view(), name='detail'),
    path('admin/', admin.site.urls),
]
