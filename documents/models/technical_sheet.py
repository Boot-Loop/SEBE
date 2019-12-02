from django.db import models
from django.utils import timezone

from rest_framework import serializers

from projects.models.project import Project

class TechnicalSheet(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ## other data

    ## auto save time
    ''' ## incase if auto_now, auto_now_add work
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(TechnicalSheet, self).save(*args, **kwargs)
    '''


## serializers
class TechnicalSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalSheet
        fields = ['id', 'project']
