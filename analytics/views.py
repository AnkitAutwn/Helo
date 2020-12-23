from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request,'analytics/about.html',{'title' : 'About'})

@login_required
def home(request):
    context = {}
    if request.user.is_superuser:
        context['readings'] = reading.objects.all().order_by('-date')
    else:
        context['readings'] = reading.objects.filter(user = request.user).order_by('-date')
    context['title'] = 'Home'
    return render(request,'analytics/home.html',context)


