# forms.py
from django import forms
from .models import Project, Task, Resource


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'status', 'due_date', 'end_date', 'assigned_to']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'status', 'due_date', 'end_date', 'assigned_to']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'manager', 'status']


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'


class ResourceCreationForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description', 'resource_type', 'availability', 'category', 'cost']
