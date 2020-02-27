from django.db import models

from projects.models.project import Project

class Quotation(models.Model):
    id          = models.IntegerField(primary_key=True)
    project     = models.ForeignKey(Project, models.CASCADE)
    document    = models.FileField(upload_to='documents/quotations/', null=True, blank=True)
    is_client   = models.BooleanField()
    comments    = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'quotation'
        verbose_name_plural = 'quotations'