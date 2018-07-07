from django.urls import path

from teachers_toolkit.grading_system.views import GradeAssingmentView

app_name = "grading_system"
urlpatterns = [

    path("grade/<int:pk>/", view=GradeAssingmentView.as_view(), name="grading"),
]
