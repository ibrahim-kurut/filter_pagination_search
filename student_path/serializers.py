from rest_framework import serializers

from .models import Path, Student


class PathSerializer(serializers.ModelSerializer):

    #? Get the path and all students in this path 
    students = serializers.SerializerMethodField()

    class Meta:
        model = Path
        fields = '__all__'
        read_only_fields = ["id"]

    #? Get the path and all students in this path 
    def get_students(self,obj):
        students = obj.students.all()
        serializer = StudentSerializer(students, many=True)
        return serializer.data
        


class StudentSerializer(serializers.ModelSerializer):

    # for show the student's path
    path_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ["id"]

    # for show the student's path
    def get_path_name(self,obj):
        return obj.path.path_name
