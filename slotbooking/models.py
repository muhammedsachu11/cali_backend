from django.db import models

# Create your models here.

from django.dispatch import receiver
from django.urls import reverse





class SlotAsscTime(models.Model):
    slot_assc_pers_id = models.AutoField(primary_key=True)
    user_assc_id = models.IntegerField(blank=True, null=True)
    slot_timing = models.CharField(max_length=20)
    
   

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    # token = models.CharField(max_length=254)
    # first_login = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'auth_user'

class Slotdetails(models.Model):
    slot_id = models.IntegerField(primary_key=True)
    slot_detail_id = models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=50, blank=True, null=True)
    recruiter_name = models.CharField(max_length=50, blank=True, null=True)
    recruiter_id = models.IntegerField(blank=True, null=True)
    slot_timing = models.CharField(max_length=10, blank=True, null=True)
    slot_item_date = models.DateField(blank=True, null=True)
    slot_type = models.CharField(max_length=10, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    slot_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SlotDetails'



