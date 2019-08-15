from django.urls import path

from web import views

urlpatterns = [
    path("<int:pk>", views.job_posting_view),
    path("<int:pk>/<slug:slug>", views.job_posting_view, name="job-posting"),
    path("class-based/<int:pk>", views.JobsDetailView.as_view()),
    path(
        "class-based/<int:pk>/<slug:slug>",
        views.JobsDetailView.as_view(),
        name="job-posting-class-based",
    ),
]
