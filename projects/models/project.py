from django.db import models
from django.utils import timezone


from accounts.models.client import Client
from accounts.models.supplier import Supplier

class Project(models.Model): ## TODO: change on_delete

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
    
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    suppliers       = models.ManyToManyField(Supplier, blank=True)
    date            = models.DateTimeField()
    is_accepted     = models.BooleanField(default=False)
    accepted_date   = models.DateTimeField(null=True, blank=True)
    ## estimated time what type?
    ''' Technical Sheet is has project as foreign key (for one to many relation) '''

    ## other fields

    def __str__(self):
        return 'project_' + str( self.id )