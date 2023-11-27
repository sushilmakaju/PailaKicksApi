from django.contrib import admin
from .models import *
# Register your models here.


class UserDisplayModel(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name')
    list_filter = ('email', 'created_date')
    search_fields = ('first_name', 'user_type')

admin.site.register(User,UserDisplayModel)