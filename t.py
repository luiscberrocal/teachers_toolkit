# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Student, Course, StudenEnrollment, AssignmentGroup, Assignment, AssignmentResult


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'national_id')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date')
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
class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'assingment_date',
        'due_date',
        'mandatory',
        'course',
        'group',
    )
    list_filter = (
        'assingment_date',
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
