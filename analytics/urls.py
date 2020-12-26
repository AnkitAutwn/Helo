from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',  Readings.as_view() , name = 'analytics-home'),
    path('about/', views.about , name = 'analytics-about'),
    path('user/<str:username>', UserReadingView.as_view() , name = 'user-readings'),
    path('download/', download , name = 'download'),
]

