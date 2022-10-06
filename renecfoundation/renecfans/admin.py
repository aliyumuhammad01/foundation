from django.contrib import admin

from .models import *
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display =("id","state")
    

class Local_governmentAdmin(admin.ModelAdmin):
    list_display = ("state_id","local_government",)
    

class PeopleAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","state", "phone_number")

class contributorAdmin(admin.ModelAdmin):
    list_display = ("person", "amount", "reciever_phone")
admin.site.register(State, StateAdmin)
admin.site.register(Local_government, Local_governmentAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Contributor, contributorAdmin)



