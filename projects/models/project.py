from django.db import models
from django.utils import timezone


from accounts.models.client import Client
from accounts.models.supplier import Supplier

PROJECT_TYPES = [
    (1, 'INSTALLATION'),
    (2, 'MAINTENANCE'),
    (3, 'REPAIR_OR_MODERNIZATION'),
    (4, 'OTHERS'),
]

class Project(models.Model): ## TODO: change on_delete
    id              = models.IntegerField(primary_key=True)
    name            = models.CharField(max_length=40)
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    suppliers       = models.ManyToManyField(Supplier,      blank=True)
    location        = models.CharField(max_length=40,       null=True, blank=True)
    date            = models.DateTimeField(                 null=True, blank=True)
    creation_date   = models.DateTimeField(                 null=True, blank=True)
    project_type    = models.IntegerField(choices=PROJECT_TYPES)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.name