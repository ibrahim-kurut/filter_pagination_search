from django.db import models

# Create your models here.
class Path(models.Model):
    path_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.path_name

class Student(models.Model):
    path = models.ForeignKey(Path,related_name='students', on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    

    
