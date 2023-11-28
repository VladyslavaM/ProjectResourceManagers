from django.contrib.auth.models import User  # Змінено імпорт
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

# ...

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Отримання даних з форми
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Створення користувача
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Автентифікація користувача
            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)

            return redirect('base')  # Перенаправлення на домашню сторінку після реєстрації

    else:
        form = SignupForm()

    return render(request, 'login.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправлення на домашню сторінку після входу
            else:
                # Додайте обробку помилки невірного входу
                pass

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})