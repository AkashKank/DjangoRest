from rest_framework import serializers
from .models import CustomUser,NewUserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password','userchoice']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            userchoice=validated_data['userchoice']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUserModel
        fields = ['username', 'email', 'password','userchoice']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = NewUserModel(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            userchoice=validated_data['userchoice']
        )
        user.save()
        return user
    