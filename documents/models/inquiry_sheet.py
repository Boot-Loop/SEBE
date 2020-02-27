from django.db import models
from django.utils import timezone


from projects.models.project import Project

class InquirySheet(models.Model):
    id          = models.IntegerField(primary_key=True)
    project     = models.ForeignKey(Project, models.CASCADE)
    document    = models.FileField(upload_to='documents/inquiry_sheets/', null=True, blank=True)
    is_client   = models.BooleanField()
    comments    = models.TextField(null=True, blank=True)

    # created = models.DateTimeField(editable=False, auto_now_add=True)
    # last_modified = models.DateTimeField(editable=False, auto_now=True)
    

    class Meta:
        verbose_name = 'inquirysheet'
        verbose_name_plural = 'inquirysheets'

    ## auto save time
    ''' ## incase if auto_now, auto_now_add work
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.last_modified = timezone.now()
        return super(TechnicalSheet, self).save(*args, **kwargs)
    '''
