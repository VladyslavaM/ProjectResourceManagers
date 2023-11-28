#views
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, ProjectForm
from .models import Project, Task, Resource, Expense, User, Role

def task_view(request):
    # Отримайте всі задачі та розділіть їх за статусами
    todo_tasks = Task.objects.filter(status='To Do')
    doing_tasks = Task.objects.filter(status='Doing')
    done_tasks = Task.objects.filter(status='Done')

    # Передайте ці дані у контекст для відображення у шаблоні
    return render(request, 'dashboard.html', {'todo_tasks': todo_tasks, 'doing_tasks': doing_tasks, 'done_tasks': done_tasks})


def signup(request):
    if request.method != 'POST':
        form = SignupForm()
    # Відправка повідомлень і перенаправлення
    else:  # Перевірка користувача та збереження в базу даних
        form = SignupForm(request.POST)
        if form.is_valid():
            return render(request, 'login.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return
    # Перевірка користувача та автентифікація
            # Відправка повідомлень і перенаправлення
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def base(request):
    # Додайте код для обробки головної сторінки тут
    return render(request, 'base.html')

def dashboard(request):
    # Додайте код для обробки головної сторінки тут
    return render(request, 'dashboard.html')

# View для відображення списку проектів
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


# View для відображення списку завдань
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


# View для відображення списку ресурсів
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})


# View для відображення списку витрат
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})


# View для відображення списку користувачів
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


# View для відображення списку ролей
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_list', project_id=project.id)
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})
