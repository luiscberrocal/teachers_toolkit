from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from teachers_toolkit.grading_system.models import Assignment, Student, AssignmentResult


class GradeAssingmentView(TemplateView):
    template_name = 'grading_system/grading_assingment.html'


    def get_context_data(self, **kwargs):
        ctx = super(GradeAssingmentView, self).get_context_data(**kwargs)
        ctx['assignment'] = Assignment.objects.get(pk=self.kwargs['pk'])
        students = Student.objects.all()
        assignment_results = list()
        for student in students:
            result = AssignmentResult.objects.get_or_create(student=student, assignment=ctx['assignment'])[0]
            assignment_results.append(result)
        ctx['results'] = assignment_results
        return ctx

    def post(self, request):

        return super(GradeAssingmentView, self).post(request)
