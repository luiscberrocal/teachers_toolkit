import os

from decimal import Decimal
from django.core.management import BaseCommand
from openpyxl import load_workbook

from teachers_toolkit.grading_system.models import AssignmentResult


class Command(BaseCommand):
    """
        $ python manage.py
    """

    def add_arguments(self, parser):
        # parser.add_argument('requirement_filename')
        # parser.add_argument("-l", "--list",
        #                     action='store_true',
        #                     dest="list",
        #                     help="List employees",
        #                     )
        # parser.add_argument("-a", "--assign",
        #                     action='store_true',
        #                     dest="assign",
        #                     help="Create unit assignments",
        #                     )
        #
        # parser.add_argument("--office",
        #                     dest="office",
        #                     help="Organizational unit short name",
        #                     default=None,
        #                     )
        # parser.add_argument("--start-date",
        #                     dest="start_date",
        #                     help="Start date for the assignment",
        #                     default=None,
        #                     )
        # parser.add_argument("--fiscal-year",
        #                     dest="fiscal_year",
        #                     help="Fiscal year for assignments",
        #                     default=None,
        #                     )
        # parser.add_argument("-u", "--username",
        #                 dest="usernames",
        #                 help="LDAP usernames for employees",
        #                 nargs='+',
        #                 )
        pass

    def handle(self, *args, **options):
        filename = '/app/output/lista_alumnos.xlsx'
        exists = os.path.exists(filename)
        self.stdout.write('Exists: {}'.format(exists))
        wb = load_workbook(filename=filename)
        sheet = wb['notas']
        cedula_col = 2
        lab_num = 1
        grade_col = 16
        comment_col = 17

        lab_name = 'Parcial {}'.format(lab_num)

        first_name_col = 0
        last_name_col = 1

        row_num = 0

        for row in sheet.rows:
            if row_num != 0:
                student = '{}, {}'.format(row[last_name_col].value, row[first_name_col].value)
                grade = row[grade_col].value
                try:
                    result = AssignmentResult.objects.get(student__national_id=row[cedula_col].value, assignment__name=lab_name)
                    result.comments = row[comment_col].value
                    if grade is None:
                        result.grade = Decimal('0.00')
                    else:
                        result.grade = Decimal(str(grade)) * Decimal(100.0)

                    if row[comment_col].value is None:
                        result.comments = ''
                    result.save()
                    self.stdout.write('{} {} {}'.format(row_num, row[0].value, row[1].value))
                except Exception as e:
                    self.stderr.write('Error {} row {} student {}'.format(str(e), row_num, student))
                    self.stderr.write('Grade: {} {}'.format(grade, type(grade).__name__))

            row_num += 1


