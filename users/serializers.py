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
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'], phone=validated_data['phone'],
                    first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                    avatar=validated_data['avatar'], country=validated_data['country'],
                    city=validated_data['city'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'country', 'city', 'avatar']
