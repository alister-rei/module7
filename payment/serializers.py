from rest_framework import serializers

from courses.models import Course
from courses.serializers import CourseSerializer
from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from payment.models import Payment
from users.serializers import UserSerializer


# Serializers define the API representation.
class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    lesson_pay = LessonSerializer(read_only=True)
    course_pay = CourseSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['user', 'date_payment', 'lesson_pay', 'course_pay', 'payment_amount', 'payment_method']

    def create(self, validated_data):
        payment_item = Payment.objects.create(**validated_data)
        return payment_item

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.lesson_pay = validated_data.get('lesson_pay', instance.lesson_pay)
        instance.course_pay = validated_data.get('course_pay', instance.course_pay)
        instance.payment_amount = validated_data.get('payment_amount', instance.payment_amount)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)
        instance.save()
        return instance

