from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ('principal', 'Principal'),
        ('hod', 'HOD'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    
class PrincipalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class HODProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
