from rest_framework import serializers
from myapp.models import Student

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name']

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

