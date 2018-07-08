from django.urls import path

from teachers_toolkit.grading_system.views import GradeAssingmentView, AssignmentListView, StudentGradeAssingmentView, \
    GradeAssingmentListView

app_name = "grading_system"
urlpatterns = [

    path("grade/<int:pk>/", view=GradeAssingmentView.as_view(), name="grading"),
    path("student-grades/<int:pk>/", view=StudentGradeAssingmentView.as_view(), name="student-grades"),

    path("grade/not-received/<int:pk>/", view=GradeAssingmentView.as_view(),
         name="grading-not-received", kwargs={'filter': 'not-received'}),
    path("grades/course/<str:slug>/", view=GradeAssingmentListView.as_view(),
         name="grading-course"),
    path("grades/course/<str:slug>/not-received/", view=GradeAssingmentListView.as_view(),
         name="grading-course-not-received", kwargs={'filter': 'not-received'}),
    path("assignments/", view=AssignmentListView.as_view(), name="assignments-list"),

]
