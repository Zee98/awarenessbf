
from django.contrib import admin
from django.urls import path
from landingsite import views as site_views

urlpatterns = [
    path('', site_views.index, name="index"),
]
