from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('principal/dashboard/', views.principal_dashboard, name='principal_dashboard'),
    path('hod/dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
]
