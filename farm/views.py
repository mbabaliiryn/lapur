from django.shortcuts import render

from rest_framework import  viewsets
from .models import  FarmUser, UserRoles, Permissions, PermissionsRoles, Roles

from .serializers import FarmUserSerializer, UserRolesSerializer, PermissionsSerializer, PermissionsRolesSerializer, RolesSerializer







class FarmUserViewSet(viewsets.ModelViewSet):

    queryset = FarmUser.objects.all()
    serializer_class = FarmUserSerializer


class UserRolesViewSet(viewsets.ModelViewSet):

    queryset = UserRoles.objects.all()
    serializer_class = UserRolesSerializer



class PermissionsViewSet(viewsets.ModelViewSet):

    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer



class PermissionsRolesViewSet(viewsets.ModelViewSet):

    queryset = PermissionsRoles.objects.all()
    serializer_class = PermissionsRolesSerializer

    

class RolesViewSet(viewsets.ModelViewSet):

    queryset = Roles.objects.all()
    serializer_class = RolesSerializer



 
