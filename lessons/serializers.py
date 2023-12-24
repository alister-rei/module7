from rest_framework import serializers

from lessons.models import Lesson
from main.validators import use_site_link, VideoLinkValidator
from users.serializers import UserShortSerializer


# Serializers define the API representation.
class LessonSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[use_site_link])
    owner = UserShortSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video')]
