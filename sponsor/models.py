from django.db import models
from helpers import site_utils


def create_sponsor_image_filename(instance, uploaded_filename):
    return site_utils.create_file_name('sponsors', instance.name, uploaded_filename)


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    primary_url = models.URLField(null=True, blank=True)
    secondary_url = models.URLField(null=True, blank=True)
    primary_phone = models.CharField(max_length=25, null=True, blank=True)
    secondary_phone = models.CharField(max_length=25, null=True, blank=True)
    logo = models.ImageField(upload_to=create_sponsor_image_filename, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class SponsorshipInformation(models.Model):
    about = models.TextField()
    how_to = models.TextField()
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Sponsorship Information'

    def __str__(self):
        return 'Sponsorship Information'