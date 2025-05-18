from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .models import User

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on user role
            if user.role == 'principal':
                return redirect('principal_dashboard')
            elif user.role == 'hod':
                return redirect('hod_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'student':
                return redirect('student_dashboard')
        else:
            return render(request, 'core/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def principal_dashboard(request):
    return render(request, 'core/principal_dashboard.html')

@login_required
def hod_dashboard(request):
    return render(request, 'core/hod_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')
