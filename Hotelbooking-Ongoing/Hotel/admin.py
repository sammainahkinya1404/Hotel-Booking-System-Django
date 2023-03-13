from django.contrib import admin
from Hotel.models import Customers,Rooms
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['FullName', 'email','username','date_joined','last_login']
class RoomAdmin(admin.ModelAdmin):
    list_display = ['Room_name', 'Room_status']

admin.site.register(Customers, CustomerAdmin)