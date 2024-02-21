from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    profile_pic = models.ImageField(null=True, upload_to='profile_pics')

    def __str__(self):
        return self.name
