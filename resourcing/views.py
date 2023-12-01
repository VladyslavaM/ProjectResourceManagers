# views
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ProjectForm, ResourceCreationForm
from .forms import TaskCreationForm
from .forms import TaskForm
from .models import Project, Task, Resource, Expense, User, Role
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ResourceForm


@csrf_protect
@require_POST
def save_task_changes(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        field_name = request.POST.get('field')
        value = request.POST.get('value')

        try:
            task = Task.objects.get(pk=task_id)
            setattr(task, field_name, value)
            task.save()
            return JsonResponse({'status': 'success'})
        except Task.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def task_view(request):
    todo_tasks = Task.objects.filter(status='To Do')
    doing_tasks = Task.objects.filter(status='Doing')
    done_tasks = Task.objects.filter(status='Done')

    return render(request, 'dashboard.html',
                  {'todo_tasks': todo_tasks, 'doing_tasks': doing_tasks, 'done_tasks': done_tasks})


def base(request):
    return render(request, 'base.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_list', project_id=project.id)
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})


def get_task_details(request, task_id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(pk=task_id)
            data = {
                'id': task.id,
                'name': task.name,
                'due_date': str(task.due_date),
            }
            return JsonResponse(data, safe=False)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return JsonResponse({'status': 'success'})
        else:
            messages.error(request, 'Invalid form data. Please check the errors.')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    tasks.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('task_list')


def create_task(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            due_date = form.cleaned_data['due_date']
            end_date = form.cleaned_data['end_date']
            assigned_to = form.cleaned_data['assigned_to']

            task = Task.objects.create(
                project=project,
                name=name,
                description=description,
                status=status,
                due_date=due_date,
                end_date=end_date,
                assigned_to=assigned_to
            )


            return JsonResponse({'message': 'Task created successfully'})
        else:
            # Form is invalid, return errors
            return JsonResponse({'message': 'Invalid form data', 'errors': form.errors}, status=400)
    else:
        # Render the create task page with an empty form
        return render(request, 'create_task.html', {'form': TaskCreationForm()})


def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            resource_type = form.cleaned_data['resource_type']
            availability = form.cleaned_data['availability']
            category = form.cleaned_data['category']
            cost = form.cleaned_data['cost']

            resource = Resource.objects.create(
                name=name,
                description=description,
                resource_type=resource_type,
                availability=availability,
                category=category,
                cost=cost
            )


            return JsonResponse({'message': 'Resource created successfully'})
        else:
            # Form is invalid, return errors
            return JsonResponse({'message': 'Invalid form data', 'errors': form.errors}, status=400)
    else:

        return render(request, 'create_resource.html', {'form': ResourceCreationForm()})


def edit_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)

    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resource updated successfully!')
            return JsonResponse({'status': 'success'})
        else:
            messages.error(request, 'Invalid form data. Please check the errors.')
    else:
        form = ResourceForm(instance=resource)

    return render(request, 'edit_resource.html', {'form': form, 'resource': resource})


def delete_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    resource.delete()
    messages.success(request, 'Resource deleted successfully!')
    return redirect('resource_list')


def save_resource_changes(request, resource_id):
    if request.method == 'POST':
        resource = get_object_or_404(Resource, id=resource_id)
        field_name = request.POST.get('field')
        new_value = request.POST.get('value')

        if field_name and new_value:
            setattr(resource, field_name, new_value)
            resource.save()

            return JsonResponse({'status': 'success', 'message': 'Changes saved successfully.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})


# View для відображення списку користувачів
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


# View для відображення списку ролей
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})
