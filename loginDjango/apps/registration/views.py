from django.contrib import messages
from .models import User, UserManager
from django.shortcuts import render, HttpResponse, redirect
import bcrypt

def index(request):
    return render(request, 'registration/index.html')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')   
    else:
        return redirect('/success')

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')    
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print pwhash
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pwhash)
        request.session['first_name'] = request.POST['first_name']
        return redirect ('/success')

def success(request):
    
    return render(request, 'registration/success.html')


