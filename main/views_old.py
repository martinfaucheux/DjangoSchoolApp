from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import School
from main.serializers import SchoolSerializer

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


@csrf_exempt
def school_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SchoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def school_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        school = School.objects.get(pk=pk)
    except School.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SchoolSerializer(school, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        school.delete()
        return HttpResponse(status=204)