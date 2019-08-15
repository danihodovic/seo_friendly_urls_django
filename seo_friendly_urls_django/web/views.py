from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView

from .models import JobPosting


def job_posting_view(request, pk, slug):
    job = get_object_or_404(JobPosting, pk=pk)
    html = f"""
        <html>
        <body>
        <h1>{job.role} at {job.company_name}</h1>
        </body>
        </html>
    """
    return HttpResponse(html)


class JobsDetailView(DetailView):
    model = JobPosting

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.path != self.object.get_absolute_url():
            return redirect(self.object, permanent=True)

        return super().get(self, request, args, kwargs)
