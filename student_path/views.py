from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer
from .paginations import (
    Custom_Pagination_Student, 
    Custom_Pagination_Path,

    Custom_Limit_Offset_Student,
    Custom_Limit_Offset_Path,

    Custom_Cursor_Pagination
    )

class PathModelViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    # pagination_class = Custom_Pagination_Path
    # pagination_class = Custom_Limit_Offset_Path


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = Custom_Pagination_Student
    # pagination_class = Custom_Limit_Offset_Student
    pagination_class = Custom_Cursor_Pagination
