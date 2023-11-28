#models
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    manager = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    due_date = models.DateField()

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    resource_type = models.CharField(max_length=20)
    availability = models.PositiveIntegerField()
    category = models.CharField(max_length=50, blank=True, null=True)  # Категорія ресурсу
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Вартість ресурсу

    def __str__(self):
        return self.name

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    roles = models.ManyToManyField('Role')

class Role(models.Model):
    name = models.CharField(max_length=20)
