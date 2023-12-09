from rest_framework import serializers

from courses.models import Course


# Serializers define the API representation.
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
