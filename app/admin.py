from django.contrib import admin
from .models import dress_effects, fire_effects

# Register your models here.


class AdminDressEffects(admin.ModelAdmin):
    list_display = ['id', 'status']


class AdminFireEffects(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']


admin.site.register(dress_effects, AdminDressEffects)
admin.site.register(fire_effects, AdminFireEffects)
