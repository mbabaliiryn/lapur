from rest_framework import serializers

from .models import FarmUser, UserRoles, Permissions ,PermissionsRoles, Roles






class FarmUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmUser
        fields = '__all__'



class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'



class PermissionsRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionsRoles
        fields = '__all__'



class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'










