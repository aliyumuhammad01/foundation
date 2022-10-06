
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from . models import *
# Create your views here.

def index(request):
    #lg = Local_government.objects.values('state_id_id').annotate(Count('local_government')).order_by()
    if request.user.is_authenticated:
        st_count = State.objects.count()
        memeber_count = People.objects.count()
        #state_total = 
        user = request.user
        return render(request, 'renecfans/dashboard.html', {
        "message":f"Hi! {user} welcome back ",
        "States":st_count,
        "members":memeber_count
        }
    )
    
    else:
        return redirect('/signup')


def signup(request):
 
    if request.user.is_authenticated:
        return redirect('/index')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/index')
         
        else:
            return render(request,'renecfans/signup.html',{
            
            
            'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'renecfans/signup.html',{'form':form})
def signin(request):
    if request.user.is_authenticated:
        return redirect('/index')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/index')
        else:
            form = AuthenticationForm()
            return render(request,'renecfans/signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'renecfans/signin.html', {'form':form})

    from django.contrib.auth import logout 

from . models import *

def signout(request):
    logout(request)
    return redirect('/signin')



 







