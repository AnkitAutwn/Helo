from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
import csv  

def about(request):
    return render(request,'analytics/about.html',{'title' : 'About'})

@login_required
def home(request):
    context = {}
    if request.user.is_superuser or request.user.is_staff:
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
        if self.request.user.is_superuser or self.request.user.is_staff:
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
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False

@login_required
def download(request):
    if request.user.is_superuser or request.user.is_staff:
        readings = reading.objects.all().order_by('-date')
    else:
        readings = reading.objects.filter(user = request.user).order_by('-date') 
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="report.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['Name','Time-Stamp','Temperature','Oxygen Level','Pulse Rate','Mask Verified','Identity Verified'])  
    for read in readings:
        writer.writerow([read.user.username, read.date.strftime("%d-%b-%Y (%H:%M:%S)") , float(read.temperature), float(read.spo2), float(read.pulse_rate), read.mask_verified, read.identity_verfied])
    return response



