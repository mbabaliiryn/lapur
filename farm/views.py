from django.shortcuts import render

from rest_framework import  viewsets, permissions
from .models import  FarmUser, UserRole, FieldWorker, FarmerGroup, Farmer
from .serializers import FarmUserSerializer, UserRoleSerializer, FieldWorkerSerializer, FarmerGroupSerializer, FarmerSerializer
from rest_framework import mixins
# from rest_framework import generics



class FarmUserViewSet(viewsets.ModelViewSet):

    queryset = FarmUser.objects.all()
    serializer_class = FarmUserSerializer

   

class UserRoleViewSet(viewsets.ModelViewSet):

    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    


class FieldWorkerViewSet(viewsets.ModelViewSet):

    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class FarmerGroupViewSet(viewsets.ModelViewSet):

    queryset = FarmerGroup.objects.all()
    serializer_class = FarmerGroupSerializer
    



class FarmerViewSet(viewsets.ModelViewSet):

    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
 
 