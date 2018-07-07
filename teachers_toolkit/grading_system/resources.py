from import_export import resources

from teachers_toolkit.grading_system.models import Student


class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'national_id', 'email')
        export_order = ('id', 'first_name', 'last_name', 'national_id', 'email')
