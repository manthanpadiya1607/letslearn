from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import profile



# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['passw']

        user = auth.authenticate(username=username, password=passw)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")



def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email_id = request.POST['email_id']
        passw = request.POST['passw']

        if User.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect('register')
        elif User.objects.filter(email=email_id).exists():
            messages.info(request,"Email-id already registered")
            return redirect('register')



        else:
            signup = User.objects.create_user(username=username, first_name=name, email=email_id,password=passw)
            signup.save()

        print("User Created")
        return redirect('login')




    else:
        return render(request, 'register.html')

def addfriend(request):

    Profiles = profile.objects.get(user=request.user)
    context = {'Profiles':Profiles}
    return render(request, 'addfriend.html')

