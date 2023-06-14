from django.contrib import admin
from .models import status

# Register your models here.


class AdminStatus(admin.ModelAdmin):
    list_display = ['id', 'status']


admin.site.register(status, AdminStatus)
