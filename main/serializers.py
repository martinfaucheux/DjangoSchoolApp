from rest_framework import serializers
from main.models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
  class Meta:
    model = School
    fields = ['id', 'name', 'max_numb']


class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'last_name', 'str_id', 'creation_date', 'birthday', 'school']