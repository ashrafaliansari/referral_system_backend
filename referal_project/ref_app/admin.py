from django.contrib import admin
from django.contrib.auth.models import User
from .models import SignUp,SignUp2
# @admin.register(User)
admin.site.register(SignUp)
admin.site.register(SignUp2)
# Register your models here.