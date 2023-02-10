from django.db import models

from users.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
