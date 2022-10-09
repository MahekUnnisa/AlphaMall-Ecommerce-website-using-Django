from django.shortcuts import render
from .models import Product, Contact
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from math import ceil
# Create your views here.
def productView(request, myid):
    
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'prodView.html', {'product':product[0]})

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername', False)
        loginpassword = request.POST.get('loginpassword', False)

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect('/')
        else:
            messages.success(request, 'Invalid Credentials, please try again')
            return redirect('/')
    return HttpResponse('404 - Not Found')

def handleRegister(request):
    if request.method=='POST':
        
        username = request.POST.get('username', False)
        fname  = request.POST.get('fname', False)
        lname  = request.POST.get('lname',False)
        email  = request.POST.get('email',False)
        pass1  = request.POST.get('pass1',False)
        pass2  = request.POST.get('pass2',False)
        # Create the user
        # get the post parameter
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request,"Passwords do not match")
            return redirect('/')
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect('/')
        # myuser = User(email=email, username = username, password=pass1)
        myuser = User.objects.create_user(username=username,email=email,password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You are registered successfully") 
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})

def search(request):
    return render(request, 'search.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'prodView.html', {'product':product[0]})


def tracker(request):
    return render(request, 'tracker.html')