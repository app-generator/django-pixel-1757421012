# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Data_Sources(models.Model):

    #__Data_Sources_FIELDS__
    ds_id = models.IntegerField(null=True, blank=True)
    ds_name = models.TextField(max_length=255, null=True, blank=True)
    ds_active = models.BooleanField()
    ds_upadted_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    ds_direction = models.TextField(max_length=255, null=True, blank=True)

    #__Data_Sources_FIELDS__END

    class Meta:
        verbose_name        = _("Data_Sources")
        verbose_name_plural = _("Data_Sources")


class Data_Tables(models.Model):

    #__Data_Tables_FIELDS__
    dt_ds_id = models.ForeignKey(data_sources, on_delete=models.CASCADE)
    dt_id = models.IntegerField(null=True, blank=True)
    dt_name = models.TextField(max_length=255, null=True, blank=True)
    dt_updated_at = models.TextField(max_length=255, null=True, blank=True)

    #__Data_Tables_FIELDS__END

    class Meta:
        verbose_name        = _("Data_Tables")
        verbose_name_plural = _("Data_Tables")



#__MODELS__END
