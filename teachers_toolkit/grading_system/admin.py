# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from teachers_toolkit.grading_system.resources import StudentResource
from .models import Student, Course, StudenEnrollment, AssignmentGroup, Assignment, AssignmentResult


@admin.register(Student)
class StudentAdmin(ImportExportActionModelAdmin):
    resource_class = StudentResource
    list_display = ('id', 'first_name', 'last_name', 'national_id', 'email')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name',)


@admin.register(StudenEnrollment)
class StudenEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course')
    list_filter = ('student', 'course')


@admin.register(AssignmentGroup)
class AssignmentGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight')
    search_fields = ('name',)


@admin.register(Assignment)
class AssignmentAdmin(ImportExportActionModelAdmin):
    list_display = (
        'id',
        'name',
        'assignment_date',
        'due_date',
        'mandatory',
        'course',
        'group',
    )
    list_filter = (
        'assignment_date',
        'due_date',
        'mandatory',
        'course',
        'group',
    )
    search_fields = ('name',)


@admin.register(AssignmentResult)
class AssignmentResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'assignment', 'student', 'grade', 'comments')
    list_filter = ('assignment', 'student')
