from django.db import models
from django.contrib.auth.models import User


#This is the model for the notes also called tasks
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

#This is the model for a todo list item
class Todo(models.Model):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # parent_todo = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']

#This is the subtask model
class Subtask(models.Model):
    name = models.CharField(max_length=255)
    parent_todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.name