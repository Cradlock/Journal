from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name","surname",)
    list_filter = ("point",)
    search_fields = ("id","name","surname")

class TruancyAdmin(admin.ModelAdmin):
    list_display = ("student",)
    list_filter = ("date",)


admin.site.register(Student,StudentAdmin)
admin.site.register(Truancie,TruancyAdmin)

