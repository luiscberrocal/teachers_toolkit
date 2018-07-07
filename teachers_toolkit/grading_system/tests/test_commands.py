from django.core.management import call_command
from django.test import TestCase


class CommandsTestCase(TestCase):
    def test_mycommand(self):
        " Test my custom command."

        args = []
        opts = {}
        call_command('load_grades', *args, **opts)
