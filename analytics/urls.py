from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home , name = 'analytics-home'),
    path('about/', views.about , name = 'analytics-about')
]

