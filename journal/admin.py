from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name","surname",)
    list_filter = ("point",)
    search_fields = ("id","name","surname")
    actions = ('reset_points',)

    def reset_points(self,request,queryset):
        queryset.update(point=0)
        self.message_user(request,"Баллы были обнулены")


class TruancyAdmin(admin.ModelAdmin):
    list_display = ("student",)
    list_filter = ("date",)
    list_per_page = 6

class RuleAdmin(admin.ModelAdmin):
    list_filter = ("date","version")
    readonly_fields = ("version",)
    




admin.site.register(Student,StudentAdmin)
admin.site.register(Truancie,TruancyAdmin)
admin.site.register(Rules,RuleAdmin)
