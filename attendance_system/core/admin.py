from django.contrib import admin
from .models import User, PrincipalProfile, HODProfile, TeacherProfile, StudentProfile

# Register your models here.


admin.site.register(User)
admin.site.register(PrincipalProfile)
admin.site.register(HODProfile)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
