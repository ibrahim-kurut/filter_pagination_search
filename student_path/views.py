from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer


class PathModelViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
