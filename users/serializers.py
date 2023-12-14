from users.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'phone', 'country', 'city',
                  'avatar']


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone', 'country', 'city', 'avatar']

    def create(self, validated_data):
        user = User(email=validated_data['email'], phone=validated_data['phone'],
                    first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                    avatar=validated_data['avatar'], country=validated_data['country'],
                    city=validated_data['city'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # now password not redact
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
