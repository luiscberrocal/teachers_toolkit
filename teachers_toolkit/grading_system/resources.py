from import_export import resources

from teachers_toolkit.grading_system.models import Student, Assignment


class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'national_id', 'email')
        export_order = ('id',  'last_name', 'first_name', 'national_id', 'email')


class AssignmentResource(resources.ModelResource):

    class Meta:
        model = Assignment
        fields = ('id', 'name', 'assignment_date', 'due_date', 'mandatory', 'course', 'group')
        export_order = ('id', 'name', 'assignment_date', 'due_date', 'mandatory', 'course', 'group')

