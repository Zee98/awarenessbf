from django.contrib import admin
from django.urls import path, include
from coming import views as coming_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coming_views.coming, name="coming_soon"),
    path('subscribe', coming_views.subscribe, name="subscribe"),
]
