from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from main import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewSet, basename='school')
router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = router.urls
