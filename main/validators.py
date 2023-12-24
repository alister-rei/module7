from rest_framework import serializers

from subs.models import Sub


def use_site_link(value):
    if 'https://www.youtube.com/' not in value.lower():
        if 'https://' in value.lower():
            raise serializers.ValidationError('Разрешены только ссылки на youtube')


class VideoLinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # Извлекаем значение по ключу из словаря
        tmp_val = value.get(self.field)

        if tmp_val:
            if 'https://www.youtube.com/' not in tmp_val:
                raise serializers.ValidationError('Разрешены только ссылки на youtube')
