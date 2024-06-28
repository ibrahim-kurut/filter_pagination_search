from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter


from django_filters.rest_framework import DjangoFilterBackend


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
    pagination_class = Custom_Pagination_Path
    # pagination_class = Custom_Limit_Offset_Path


    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["path_name"]

    search_fields = ["path_name"] # ------------------>> from global


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = Custom_Pagination_Student
    # pagination_class = Custom_Limit_Offset_Student
    # pagination_class = Custom_Cursor_Pagination

    # filterset_fields = ["f_name"]  ------------------>>  for global
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ["f_name", "l_name", "path"]
    search_fields = ["f_name"]



    


