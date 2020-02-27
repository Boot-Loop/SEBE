'''
from django.db import models
from django.contrib.auth.models import User


## staffs will be created by superuser
class Staff(models.Model):
    email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.user.delete(*args, **kwargs) ## this will delete the staff

    def __str__(self):
        return self.user.username


#'''

