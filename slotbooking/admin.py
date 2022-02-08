from django.contrib import admin

# Register your models here.
from slotbooking.models import SlotAsscTime, Slotdetails, AuthUser

admin.site.register(SlotAsscTime)
# admin.site.register(SlotList)
admin.site.register(Slotdetails)
admin.site.register(AuthUser)
