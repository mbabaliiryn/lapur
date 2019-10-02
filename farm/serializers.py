from rest_framework import serializers

from .models import FarmUser, UserRole, FieldWorker, FarmerGroup, Farmer





class FarmUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmUser
        fields = '__all__'



class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'


class FieldWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldWorker
        fields = '__all__'



class FarmerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerGroup
        fields = '__all__'




class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'