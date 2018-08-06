from import_export import resources

from teachers_toolkit.grading_system.models import Student, Assignment, AssignmentResult


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'national_id', 'email')
        export_order = ('id', 'last_name', 'first_name', 'national_id', 'email')


class AssignmentResource(resources.ModelResource):
    class Meta:
        model = Assignment
        fields = ('id', 'name', 'assignment_date', 'due_date', 'mandatory', 'course', 'group')
        export_order = ('id', 'name', 'assignment_date', 'due_date', 'mandatory', 'course', 'group')


class AssignmentResultResource(resources.ModelResource):
    student_name = resources.Field()

    class Meta:
        model = AssignmentResult
        fields = ('id', 'student', 'assignment__group__name',
                  'student_name',
                  'assignment__name', 'grade', 'comments', 'assignment__mandatory')
        export_order = ('id', 'student', 'assignment__group__name',
                        'student_name',
                        'assignment__name', 'grade', 'comments',
                        'assignment__mandatory')

    def dehydrate_student_name(self, result):
        return '{}, {}'.format(result.student.last_name, result.student.first_name)
