from rest_framework import serializers

from courses.models import Course
from lessons.models import Lesson
from users.models import User


# Serializers define the API representation.
class CourseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class CourseLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'image', 'video']


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    lessons = CourseLessonsSerializer(many=True)
    lessons_count = serializers.IntegerField(read_only=True, source='lessons.all.count')
    # owner = CourseUserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        lessons = validated_data.pop('lessons')

        course_item = Course.objects.create(**validated_data)

        for lesson in lessons:
            Lesson.objects.create(**lesson, course=course_item)

        return course_item

    def update(self, instance, validated_data):
        lessons_data = validated_data.pop('lessons', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)

        Lesson.objects.filter(course=instance).delete()

        # пока будет так
        for lesson_data in lessons_data:
            Lesson.objects.create(**lesson_data, course=instance)

        return instance
