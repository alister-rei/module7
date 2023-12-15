from rest_framework import serializers

from lessons.models import Lesson


# Serializers define the API representation.
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
