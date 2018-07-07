from django.urls import path

from teachers_toolkit.grading_system.views import GradeAssingmentView, AssignmentListView

app_name = "grading_system"
urlpatterns = [

    path("grade/<int:pk>/", view=GradeAssingmentView.as_view(), name="grading"),
    path("grade/not-received/<int:pk>/", view=GradeAssingmentView.as_view(),
         name="grading-not-received", kwargs={'filter': 'not-received' }),
    path("assignments/", view=AssignmentListView.as_view(), name="assignments-list"),

]
