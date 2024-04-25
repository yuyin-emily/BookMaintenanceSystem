from django.contrib import admin

from account.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("studentId","reister_year","phone_number","gender","birth_date")
    list_filter = ("studentId","gender")
    search_fields = ("studentId",)
    ordering = ("studentId",)
    
admin.site.register(Student,StudentAdmin)