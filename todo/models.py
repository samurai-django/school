from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    # author = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=True)


    def __str__(self):
        return self.title

