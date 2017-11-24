from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    u = User.objects.all()
    print u
    context = {
        'puppy':u,
    }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, "users/new.html")

def edit(request, user_id):
    u = User.objects.get(id=user_id)
    print u
    context = {
        'User':u,
    }
    return render(request, "users/edit.html", context)

def show(request, user_id):
    u = User.objects.get(id=user_id)
    print u
    context = {
        'User':u,
    }
    return render(request, "users/show.html", context)

def create(request):
    if request.method == 'POST':
        u = User.objects.create(first_name =request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        print u
        user_id = str(u.id)
    return redirect ('/users/'+user_id)
def destroy(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect ('/users')
def update(request, user_id):
    u = User.objects.get(id=user_id)
    if request.method == 'POST':
        u.first_name =request.POST['first_name'] 
        u.last_name = request.POST['last_name']
        u.email = request.POST['email']
        u.save()
        print u
        user_id = str(u.id)
    return redirect ('/users/'+user_id)

# Create your views here.
