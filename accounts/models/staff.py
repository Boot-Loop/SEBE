from django.db import models
from django import forms

from django.contrib.auth.models import User

## staffs will be created by superuser
class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

## forms ##################################

from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
    )