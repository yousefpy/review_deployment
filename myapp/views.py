from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from myapp.models import Student
from .serializers import StudentListSerializer ,StudentDetailSerializer , CreateStudentSerializer

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer

class StudentDetailsView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'student_id'

class StudentUpdateView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'student_id'

class StudentDeleteView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'student_id'