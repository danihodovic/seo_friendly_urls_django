from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class JobPosting(models.Model):
    company_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def get_absolute_url(self):
        slug = slugify(f"{self.role}-at-{self.company_name}")
        return reverse("job-posting", kwargs={"pk": self.id, "slug": slug})
