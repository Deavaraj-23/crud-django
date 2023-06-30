from django.contrib import admin
from app1.models import regist

# Register your models here.

class registerAdmin(admin.ModelAdmin):
    list_display=['name','contact','address','mail']
admin.site.register(regist,registerAdmin)
