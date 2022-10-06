from django.db import models
from django.db.models import Count
from datetime import date


# Create your models here.
from django.db import models

# Create your models here.

class State(models.Model):
    state = models.CharField(max_length=60, unique = True, null=False)
    

class Local_government(models.Model):
    local_government =models.CharField(max_length=60, unique= True, null= False)
    state_id =models.ForeignKey(State, on_delete=models.CASCADE, related_name='mystate')
    

   

class People(models.Model):
    first_name = models.CharField(max_length=60,null=False)
    last_name  = models.CharField(max_length=60,  null=False)
    phone_number  = models.CharField(max_length=11, unique = True, null=False)
    nin  = models.IntegerField(11, unique=True, null=False)
    email  = models.CharField(max_length=60, unique=True, null=False)
    state = models.ForeignKey(State, to_field='id', on_delete=models.CASCADE, related_name="locality")



    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Contributor(models.Model):
    person = models.ForeignKey(People, to_field='nin', on_delete=models.CASCADE, related_name="contributor")
    amount = models.IntegerField(default=00)
    reciever_phone =models.ForeignKey(People, to_field='phone_number', on_delete=models.CASCADE, related_name="reciever")

