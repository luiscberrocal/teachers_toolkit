from django.db import models


# Create your models here.
from django_extensions.db.fields import AutoSlugField


class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    national_id = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

    class Meta:
        ordering = ('last_name', 'first_name')


class Course(models.Model):
    name = models.CharField(max_length=60)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    slug = AutoSlugField(populate_from=['name'])

    def __str__(self):
        return self.name


class StudenEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class AssignmentGroup(models.Model):
    name = models.CharField(max_length=60)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{} {}'.format(self.name, self.weight)


class Assignment(models.Model):
    name = models.CharField(max_length=60)
    assignment_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    mandatory = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    group = models.ForeignKey(AssignmentGroup, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('due_date',)


class AssignmentResult(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    grade = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    comments = models.TextField()

