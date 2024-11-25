from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Result

class UserSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        write_only_fields = ['password']
        extra_kwargs = {
            'password': {'write_only': True}
        }