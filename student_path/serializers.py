from rest_framework import serializers

from .models import Path, Student


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'
        read_only_fields = ["id"]


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
