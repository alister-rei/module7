from users.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'phone', 'country', 'city',
                  'avatar']


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'country', 'city', 'avatar']
