from django.contrib import admin
from .models import *

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'cid')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'sid', 'cid', 'prof', 'partial')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('sid', 'rollno', 'date', 'status')

@admin.register(StudentList)
class StudentListAdmin(admin.ModelAdmin):
    list_display = ('lid', 'name')
