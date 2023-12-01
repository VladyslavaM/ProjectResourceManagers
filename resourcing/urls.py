from django.urls import path

from resourcing import views
from .views import create_project




urlpatterns = [
    path('', views.base, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.project_list, name='project_list'),
    path('tasks/', views.task_list, name='task_list'),
    path('resources/', views.resource_list, name='resource_list'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('users/', views.user_list, name='user_list'),
    path('roles/', views.role_list, name='role_list'),
    path('create_project/', create_project, name='create_project'),
    path('project_list/<int:project_id>/', views.project_list, name='project_list'),
    path('get_task_details/<int:task_id>/', views.get_task_details, name='get_task_details'),
    path('save_task_changes/', views.save_task_changes, name='save_task_changes'),
    path('tasks/new/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('resources/new/', views.create_resource, name='create_resource'),
    path('resources/<int:resource_id>/edit/', views.edit_resource, name='edit_resource'),
    path('resources/<int:resource_id>/delete/', views.delete_resource, name='delete_resource'),
    path('resources/<int:resource_id>/save_changes/', views.save_resource_changes, name='save_resource_changes'),

]
