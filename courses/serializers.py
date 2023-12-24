from rest_framework import serializers

from courses.models import Course
from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from main.validators import use_site_link
from subs.models import Sub
from users.serializers import UserShortSerializer


# Serializers define the API representation.

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, required=False)
    lessons_count = serializers.IntegerField(read_only=True, source='lessons.all.count')
    owner = UserShortSerializer(read_only=True)
    description = serializers.CharField(validators=[use_site_link])
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        lessons = validated_data.pop('lessons', [])

        course_item = Course.objects.create(**validated_data)

        if lessons:
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

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Sub.objects.filter(user=request.user, course=obj, is_active=True).exists()
        return False
