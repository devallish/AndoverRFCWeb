from django.db import models
from news.models import NewsArticle
from fixture.models import Fixture
from person.models import Person
from helpers import site_utils
from sponsor.models import Sponsor


def create_squad_photo_file_name(instance, uploaded_filename):
    return site_utils.create_file_name('squads', instance.name, uploaded_filename)

class SquadSelectionItem(models.Model):
    person = models.OneToOneField(Person, primary_key=True)
    position_number = models.IntegerField()

    def display_name(self):
        return '%s %s' % (self.position_number, self.person.display_name())

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()


class SquadSelection(models.Model):
    fixture = models.OneToOneField(Fixture, primary_key=True)
    players = models.ManyToManyField(SquadSelectionItem)

    def display_name(self):
        return self.fixture.display_name()

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()

    def split_players(self):
        all_players = self.players.order_by('position_number').all()
        player_count = all_players.count()
        if player_count > 0:
            halfway = int(player_count / 2)
            players_split = {'Left': all_players[0:halfway], 'Right': all_players[halfway:]}
            return players_split

class SquadRole(models.Model):
    name = models.CharField(max_length=50)
    information = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class SquadPersonRole(models.Model):
    role = models.OneToOneField(SquadRole)
    person = models.OneToOneField(Person)
    display_position = models.IntegerField()

    def display_name(self):
        name = str(self.display_position)
        name += ': '
        if self.role:
            name += self.role.name
        else:
            name += '<role missing>'

        name += ' '

        if self.person:
            name += self.person.display_name()
        else:
            name += '<person missing>'

        return name

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()


class Squad(models.Model):
    name = models.CharField(max_length=50)
    information = models.TextField()
    squad_photo = models.ImageField(upload_to=create_squad_photo_file_name, null=True, blank=True)
    news_articles = models.ManyToManyField(NewsArticle, null=True, blank=True)
    fixtures = models.ManyToManyField(Fixture, null=True, blank=True)
    people = models.ManyToManyField(SquadPersonRole, null=True, blank=True)
    sponsors = models.ManyToManyField(Sponsor, null=True, blank=True)
    selection = models.ManyToManyField(SquadSelection, null=True, blank=True)

    def display_name(self):
        return self.name

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()