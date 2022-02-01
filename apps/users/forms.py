from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.forms.utils import ErrorList
from django.contrib.auth import authenticate
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from collections import OrderedDict as SortedDict
from s3direct.widgets import S3DirectWidget


class DivErrorList(ErrorList):

    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return u''
        return u'%s' % ''.join([u'%s' % e for e in self])


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, max_length=150, widget=forms.EmailInput(attrs={'class': "fadeIn second", 'placeholder': "Email address"}))
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'class': "fadeIn third", 'placeholder': "Password"}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError('invalid_login')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('inactive')
        return self.cleaned_data
