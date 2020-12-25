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
    return render(request,'analytics/index.html',context)


class Readings(LoginRequiredMixin, ListView):
    model = reading
    template_name = 'analytics/index.html'
    context_object_name = 'readings'
    paginate_by = 6
    def get_queryset(self):
        if self.request.user.is_superuser:
            return reading.objects.all().order_by('-date')
        else:
            return reading.objects.filter(user = self.request.user).order_by('-date')

class UserReadingView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = reading
    template_name = 'analytics/index.html' #<app><model>_<viewtype>.html
    context_object_name = 'readings'
    #ordering = ['-date_posted']
    paginate_by = 6
    
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return reading.objects.filter(user=user).order_by('-date')  

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False



