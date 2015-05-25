from django.db import models
from helpers import site_utils


def create_person_image_file_name(instance, uploaded_filename):
    return site_utils.create_file_name('people', instance.display_name, uploaded_filename)


class Person(models.Model):
    surname = models.CharField(max_length=50)
    forenames = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    image = models.ImageField(upload_to=create_person_image_file_name, null=True, blank=True)

    def display_name(self):
        return self.forenames + ' ' + self.surname

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()