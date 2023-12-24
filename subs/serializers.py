from rest_framework import serializers

from subs.models import Sub
from users.serializers import UserShortSerializer


class SubSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = Sub
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}  # Пользователь должен автоматически получаться из запроса
        }
