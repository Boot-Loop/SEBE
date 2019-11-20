from django.db import models
from django import forms
from django.contrib.auth.models import User

from rest_framework import serializers

## staffs will be created by superuser
class Staff(models.Model):
    email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.user.delete(*args, **kwargs) ## this will delete the staff

    def __str__(self):
        return self.user.username


## serialize ##############################
## TODO use custom serializer
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Staff
        fields = [ 'email', 'user' ]

## forms ##################################

from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

## only for the use of admin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation
class StaffCreationForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
    )
    email = forms.EmailField(label='Email Address')
    password1 = forms.CharField(
        label='password',
        strip=False,
        widget=forms.PasswordInput,
        validators=[password_validation.validate_password],
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput,
        help_text="Enter the same password as before, for verification."
    )

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Your Passwords didn't match")
        if User.objects.filter(email=cleaned_data.get('email')).count() > 0:
            raise forms.ValidationError("Email Already Exists")
        if User.objects.filter(username=cleaned_data.get('username')).count() > 0:
            raise forms.ValidationError("UserName Already Exists")
        return cleaned_data

