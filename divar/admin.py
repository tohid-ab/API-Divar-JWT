from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Center)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(TestModel)
class TestForm(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Home)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['advertising', 'title', 'slug', 'metrazh', 'tedad_room', 'price_to_metrazh', 'price']
    prepopulated_fields = {'slug': ('title',)}\


@admin.register(Car)
class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}\


@admin.register(Electronic)
class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
