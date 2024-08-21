from django.contrib import admin
from . import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','subcategory','category']

class AppAdmin(admin.ModelAdmin):
    list_display = ['id','app_name','app_link','app_image','category','subcategory']

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.SubCategory, SubCategoryAdmin)
admin.site.register(models.App, AppAdmin)
