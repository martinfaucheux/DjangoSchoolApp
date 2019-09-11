from main.models import School, Student
from main.serializers import SchoolSerializer, StudentSerializer
from rest_framework import viewsets, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from django.shortcuts import render



class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = School.objects.all() # order by... ?
    serializer_class = SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get_queryset(self):
    if 'school_pk' in self.kwargs:
      return Student.objects.filter(school=self.kwargs['school_pk'])
    return Student.objects.all()


  def create(self, request, school_pk=None):

    # if creation from route /schools/X/students/
    if school_pk:
      request.data["school"] = school_pk

    # normal behavior
    return super(viewsets.ModelViewSet, self).create(request)



# see:
#  https://blog.apptension.com/2017/09/13/rest-api-using-django-rest-framework/



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