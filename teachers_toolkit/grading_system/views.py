import re
from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from teachers_toolkit.grading_system.models import Assignment, Student, AssignmentResult, Course


class AssignmentListView(LoginRequiredMixin, ListView):
    model = Assignment
    context_object_name = 'assignments'

    def get_queryset(self):
        qs = super(AssignmentListView, self).get_queryset()
        if self.kwargs.get('filter') == 'not-received':
            return qs.filter(grade=Decimal('0.0'))
        return qs

class GradeAssingmentListView(LoginRequiredMixin, ListView):
    """
    http://127.0.0.1:8000/grading_system/grades/course/introduccion-a-las-herramientas-sig/
    """
    template_name = 'grading_system/assingment_result_list.html'
    model = AssignmentResult
    context_object_name = 'results'
    paginate_by = 20

    def get_queryset(self):
        qs = super(GradeAssingmentListView, self).get_queryset().select_related(
            'student', 'assignment', 'assignment__course')
        course = Course.objects.get(slug=self.kwargs['slug'])
        if self.kwargs.get('filter') == 'not-received':
            return qs.filter(
                assignment__course=course, grade=Decimal('0.0')).order_by(
                'student__last_name', 'student__first_name', 'assignment__assignment_date')
        else:
            return qs.select_related('student', 'assignment').filter(assignment__course=course)



class GradeAssingmentView(LoginRequiredMixin, TemplateView):
    template_name = 'grading_system/grading_assingment.html'

    def get_context_data(self, **kwargs):
        ctx = super(GradeAssingmentView, self).get_context_data(**kwargs)
        ctx['assignment'] = Assignment.objects.get(pk=self.kwargs['pk'])
        if  self.kwargs.get('create'):

            students = Student.objects.all()
            assignment_results = list()
            for student in students:
                result = AssignmentResult.objects.get_or_create(student=student, assignment=ctx['assignment'])[0]

                if kwargs.get('filter') == 'not-received':
                    if result.grade == Decimal('0.0'):
                        assignment_results.append(result)
                else:
                    assignment_results.append(result)
            ctx['results'] = assignment_results
        else:
            if kwargs.get('filter') == 'not-received':
                ctx['results'] = AssignmentResult.objects.filter(
                    assignment=ctx['assignment'],
                    grade=Decimal('0.0')).order_by('student__last_name', 'student__first_name')
            else:
                ctx['results'] = AssignmentResult.objects.filter(
                    assignment=ctx['assignment']).order_by('student__last_name', 'student__first_name')
        return ctx

    def post(self, request, *args, **kwargs):
        # assignment = Assignment.objects.get(pk=self.kwargs['pk'])
        regexp = re.compile(r'^grade_student_(\d+)$')
        for key, value in request.POST.items():
            match = regexp.match(key)
            if match:
                student_pk = int(match.group(1))
                comment_key = 'comment_student_{}'.format(student_pk)
                assignment_result_pk_key = 'assignment_result_pk_{}'.format(student_pk)
                # student = Student.objects.get(pk=student_pk)
                comment = request.POST[comment_key]
                assingment_result_pk = int(request.POST[assignment_result_pk_key])
                result = AssignmentResult.objects.get(id=assingment_result_pk)

                result.comments = comment
                result.grade = Decimal(value)
                result.save()
        url = reverse('grading_system:grading', kwargs={'pk': self.kwargs['pk']})
        return redirect(url)


class StudentGradeAssingmentView(LoginRequiredMixin, TemplateView):
    template_name = 'grading_system/student_grades.html'

    def get_context_data(self, **kwargs):
        ctx = super(StudentGradeAssingmentView, self).get_context_data(**kwargs)
        student_pk = self.kwargs['pk']
        results = AssignmentResult.objects.filter(student__pk=student_pk).order_by('assignment__assignment_date')
        ctx['results'] = results
        return ctx
