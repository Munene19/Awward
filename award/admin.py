from django.contrib import admin
from .models import Project,Profile

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

admin.site.register(Profile)
admin.site.register(Project)