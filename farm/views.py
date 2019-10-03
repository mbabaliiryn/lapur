from django.shortcuts import render

from rest_framework import  viewsets, permissions
from .models import  FarmUser, UserRole, FieldWorker, FarmerGroup, Farmer, Notification
from .serializers import FarmUserSerializer, UserRoleSerializer, FieldWorkerSerializer, FarmerGroupSerializer, FarmerSerializer, NotificationSerializer





class FarmUserViewSet(viewsets.ModelViewSet):

    queryset = FarmUser.objects.all()
    serializer_class = FarmUserSerializer

class Meta:
    permissions = ["only super user can delete "]

    
class UserRoleViewSet(viewsets.ModelViewSet):

    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class Meta:
    permissions = ["user can only see permissions he/she has signedup to"]
    


class FieldWorkerViewSet(viewsets.ModelViewSet):

    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer

class Meta:

    permissions = ["can signup", "can see all farmers","can create farmer groups"]



class FarmerGroupViewSet(viewsets.ModelViewSet):

    queryset = FarmerGroup.objects.all()
    serializer_class = FarmerGroupSerializer

    

class FarmerViewSet(viewsets.ModelViewSet):

    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class Meta:
    permissions = ["can signup"]
 


class NotificationViewSet(viewsets.ModelViewSet):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class Meta:
    permissions = ["can only be viewed by the super user"]
 