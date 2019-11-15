from django.db import models
from django.utils import timezone

from projects.models.project import Project

class TechnicalSheet(models.Model):
    created = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ## other data

    ## auto save time
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(TechnicalSheet, self).save(*args, **kwargs)


