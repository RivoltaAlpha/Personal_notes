from django import forms
from .models import Task,Todo,Subtask
from . import views

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','attachment',]

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'completed']

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['name']

    
    
