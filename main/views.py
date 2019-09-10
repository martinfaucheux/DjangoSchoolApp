from main.models import School, Student
from main.serializers import SchoolSerializer, StudentSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')


class SchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer




class StudentList(generics.ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer