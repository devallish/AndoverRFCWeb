from django.db import models
from squad.models import Squad


class SquadMenuItem(models.Model):
    display_name = models.CharField(max_length=20)
    ordinal_position = models.IntegerField()
    is_junior = models.BooleanField(default=True)
    squad = models.OneToOneField(Squad)

