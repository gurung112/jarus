from django.contrib import admin

# Register your models here.
class tag(admin.ModelAdmin):
    list_display=['name','email']
