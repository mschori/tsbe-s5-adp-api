from django.db import models

from users.models import User


class Module(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Grade(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    module = models.ForeignKey(Module, null=False, on_delete=models.CASCADE)
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grade
