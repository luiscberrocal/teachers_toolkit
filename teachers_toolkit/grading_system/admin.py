# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from .resources import StudentResource, AssignmentResultResource
from .models import Student, Course, StudentEnrollment, AssignmentGroup, Assignment, AssignmentResult


@admin.register(Student)
class StudentAdmin(ImportExportActionModelAdmin):
    resource_class = StudentResource
    list_display = ('id', 'first_name', 'last_name', 'national_id', 'email', 'active')
    list_editable = ('active', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'start_date', 'end_date', 'active')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name',)
    list_editable = ('active',)


@admin.register(StudentEnrollment)
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
class AssignmentResultAdmin(ImportExportModelAdmin):
    resource_class = AssignmentResultResource
    list_display = ('id', 'assignment', 'student', 'grade', 'comments')
    list_filter = ('assignment', 'student')

