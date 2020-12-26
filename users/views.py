from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import *
from recognise import add_people
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            user = User.objects.filter(username=form.cleaned_data.get('username'))[0]
            Profile.objects.create(user = user)
            verification.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html' , {'form' : form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form  = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.warning(request, f'Please Wait...')
            userform = u_form.instance
            profile = p_form.instance 
            name = userform.username
            urls = [profile.Image1.url[1:], profile.Image2.url[1:], profile.Image3.url[1:], profile.Image4.url[1:], profile.Image5.url[1:], profile.Image6.url[1:],profile.Image7.url[1:],profile.Image8.url[1:],profile.Image9.url[1:],profile.Image10.url[1:]]
            add_people.encode(urls,name)
            '''
            add_people.encode(profile.Image2.url[1:],name)
            add_people.encode(profile.Image3.url[1:],name)
            add_people.encode(profile.Image4.url[1:],name)
            add_people.encode(profile.Image5.url[1:],name)
            add_people.encode(profile.Image6.url[1:],name)
            add_people.encode(profile.Image7.url[1:],name)
            add_people.encode(profile.Image8.url[1:],name)
            add_people.encode(profile.Image9.url[1:],name)
            add_people.encode(profile.Image10.url[1:],name)
            '''
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form  = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    context['status'] = verification.objects.filter(user = request.user)[0]
    return render(request, 'users/profile.html', context)
