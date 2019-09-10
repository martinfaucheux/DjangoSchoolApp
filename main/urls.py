from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  path('schools/', views.SchoolList.as_view()),
  path('schools/<int:pk>/', views.SchoolDetail.as_view()),
  path('students/', views.StudentList.as_view()),
  path('students/<int:pk>/', views.StudentDetail.as_view()),
]

# includes all possible format (.json, .form ....)
urlpatterns = format_suffix_patterns(urlpatterns)
