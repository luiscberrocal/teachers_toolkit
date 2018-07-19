Install
=========

This is where you write how to get a new laptop to run this project.


To run a migration, open up a second terminal and run::

   docker-compose -f local.yml run --rm django python manage.py migrate

To create a superuser, run::

   docker-compose -f local.yml run --rm django python manage.py createsuperuser
