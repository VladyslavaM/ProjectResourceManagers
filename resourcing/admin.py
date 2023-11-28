from django.contrib import admin
from .models import Project, Task, Resource, Expense, User, Role


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'manager', 'status')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assigned_to', 'status', 'due_date')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'resource_type', 'availability', 'category', 'cost')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('project', 'resource', 'amount', 'expense_date')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
