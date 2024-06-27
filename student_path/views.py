from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer
from .paginations import Custom_Pagination_Student, Custom_Pagination_Path

class PathModelViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    pagination_class = Custom_Pagination_Path


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = Custom_Pagination_Student
