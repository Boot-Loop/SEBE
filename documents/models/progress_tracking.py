from django.db import models

from projects.models.project import Project

class ClientProgress(models.Model):
    id          = models.IntegerField(primary_key=True)
    project     = models.ForeignKey(Project, models.CASCADE)
    comments    = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'progress-client-file'
        verbose_name_plural = 'progress-client-files'



class SupplierProgress(models.Model):
    id          = models.IntegerField(primary_key=True)
    project     = models.ForeignKey(Project, models.CASCADE)
    comments    = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'progress-supplier-file'
        verbose_name_plural = 'progress-supplier-files'
        