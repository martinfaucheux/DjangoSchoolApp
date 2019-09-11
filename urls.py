from django.conf.urls import url
from django.urls import include, path
from main.views import SchoolViewSet, StudentViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'students', StudentViewSet, basename='student')

schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentViewSet, basename='school-students')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(schools_router.urls)),
]