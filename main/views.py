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

  # to be fixed

  def create(self, request, school_pk=None):
    print(type(request.data))
    if school_pk:
      # print('got school_pk')
      request.data["school"] = school_pk
    print(request.data)

    return super(viewsets.ModelViewSet, self).create(request)

    #return Response(status=status.HTTP_202_ACCEPTED)


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