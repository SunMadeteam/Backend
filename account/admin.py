from django.contrib import admin
from .models import ConfirmCode, User
#from django.contrib.auth.admin import UserManager

admin.site.register(ConfirmCode)
admin.site.register(User)