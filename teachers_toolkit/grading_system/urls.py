from django.urls import path

from teachers_toolkit.grading_system.views import GradeAssingmentView, AssignmentListView

app_name = "grading_system"
urlpatterns = [

    path("grade/<int:pk>/", view=GradeAssingmentView.as_view(), name="grading"),
    path("assignments/", view=AssignmentListView.as_view(), name="assignments-list"),

]
