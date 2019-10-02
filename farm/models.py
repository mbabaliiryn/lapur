from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField




class TimestampedModel(models.Model):
    """A timestamp representing when this object was created."""

    created_at = models.DateTimeField(auto_now_add=True)
    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)




class FarmUser(AbstractUser, TimestampedModel):
    USER_TYPE_CHOICES = (
      (1, 'farmer'),
      (2, 'field_worker'),
      (3, 'ASO'),
      (4, 'credit officer'),
  )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    via_search = models.BooleanField(default=False)



   

class UserRole(TimestampedModel):
    role_name = models.CharField(('name'), null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name




class FieldWorker(TimestampedModel):
    user_name = models.CharField(max_length=20, blank=False)
    address = models.TextField(max_length=60 , null=True, blank=False)

    def __str__(self):
        return self.name



class FarmerGroup(TimestampedModel):
    name = models.CharField(('name'), null=False, blank=False, max_length=255)
    farmer_group = models.ForeignKey(
        'FarmerGroup', on_delete=models.CASCADE, parent_link=True)


    def __str__(self):
        return self.name



class Farmer(TimestampedModel):
    user_name = models.CharField(max_length=20, blank=False, null=True)
    address = models.TextField(max_length=60,blank=False)
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,null=False, blank = False
    )
    phone_number = PhoneNumberField(
        ('phone number'), null=False, blank=False, unique=True)

    def __str__(self):
        return self.name



    
    

    
    

  
  
    