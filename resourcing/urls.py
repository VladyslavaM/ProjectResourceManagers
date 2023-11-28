from django.urls import path
from resourcing import views
from resourcing import login_view
from .views import project_list
from .views import create_project


urlpatterns = [
    path('', views.base, name='base'),
    path('login/', login_view.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.project_list, name='project_list'),
    path('tasks/', views.task_list, name='task_list'),
    path('resources/', views.resource_list, name='resource_list'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('users/', views.user_list, name='user_list'),
    path('roles/', views.role_list, name='role_list'),
    path('create_project/', create_project, name='create_project'),
    path('project_list/<int:project_id>/', views.project_list, name='project_list'),
]
