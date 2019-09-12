from django.db import models
from django.core.exceptions import ValidationError
import datetime

# validator to check if max numb of school is reached
def validate_school_not_full(school):
  student_list = Student.objects.filter(school=school)
  full = len(student_list) >= school.max_numb
  if full:
    raise ValidationError("The School '%s' is already full" % school , code='school_full')


# Schools have a name (20 char max) and a maximum number of student (any positive integer)
class School(models.Model):
  name = models.CharField(max_length=20)
  max_numb = models.IntegerField(default=0)

  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ['name']




# Students have a first name, a last name, and a student identification string (20 characters max for each)
class Student(models.Model):
  name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  str_id = models.CharField(max_length=20, unique=True, editable=False, default="")
  creation_date = models.DateField(default=datetime.date.today, editable=False)
  birthday = models.DateField(default=datetime.date.today)


  # Each student object must belong to a school object
  school = models.ForeignKey(
                    School,
                    on_delete=models.CASCADE,
                    validators=[validate_school_not_full])

  def generate_str():
    students = Student.objects.all()
    if not students:
      max_id = 0
    else:
      max_id = students.order_by("-id")[0].id

    return chr(max_id + 1)


  def save(self, *args, **kwargs):
    if len(self.str_id) == 0:
      self.str_id = Student.generate_str()
    super().save(*args, **kwargs)

    



  def __str__(self):
    return self.name + " " + self.last_name


  class Meta:
    ordering = ['name']




    