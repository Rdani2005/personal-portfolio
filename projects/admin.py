from django.contrib import admin

from .models import Project, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'description', 'code_link', 'view_link', 'slug','created', 'updated']
    list_filter = ['is_active']
    list_editable = []
    prepopulated_fields = {'slug' : ('title',)}