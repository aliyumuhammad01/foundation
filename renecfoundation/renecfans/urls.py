from django.urls import path, include
from django.contrib import admin
from django.contrib import admin
from django.urls import path,include
from .views import signup,signin,signout,index
 
urlpatterns = [
    path('',index),
    path('index', index, name = "index"),
    path('signup', signup, name ='signup'),
    path('signin', signin, name = 'login'),
    path('signout', signout, name = 'logout'),
]



#from . import views

#urlpatterns =[
#    path("", views.index, name="index"),
    
        
#]