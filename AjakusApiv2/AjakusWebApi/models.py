from rest_framework import mixins
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

class Content(models.Model):
    owner = models.ForeignKey('AjakusWebApi.Profile',related_name='content', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    body =models.CharField(max_length=100,null=False)
    summary = models.CharField(max_length=100,null=False)
    upload=models.FileField(null=True,default='')

    class Meta:
        ordering = ['created']

#calling custom user model
class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True,default=None)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True) 
    phone=models.IntegerField(max_length=10,null=True)
    address=models.CharField(max_length=254, null=True)
    city=models.CharField(max_length=254, null=True)
    state=models.CharField(max_length=254, null=True)
    country=models.CharField(max_length=254, null=True)
    pincode=models.IntegerField(max_length=6, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs) 