from django.db import models
from news.models import NewsArticle
from fixture.models import Fixture
from event.models import Event
from datetime import datetime
from sponsor.models import Sponsor
from squad.models import Squad

class CarouselItem(models.Model):
    ordinal_position = models.IntegerField()
    news_article = models.OneToOneField(NewsArticle)

    def display_name(self):
        name = str(self.ordinal_position) + ': '
        if self.news_article:
            name += self.news_article.headline
        else:
            name += '<news article missing>'
        return name

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()


class Home(models.Model):
    title = models.CharField(max_length=50, default='Andover Rugby Club')
    news_articles = models.ManyToManyField(NewsArticle, null=True, blank=True)
    fixtures = models.ManyToManyField(Fixture, null=True, blank=True)
    events = models.ManyToManyField(Event, null=True, blank=True)
    carousel_items = models.ManyToManyField(CarouselItem, null=True, blank=True)
    sponsors = models.ManyToManyField(Sponsor, null=True, blank=True)

    def next_fixtures(self):
        fixtures_on_or_after_today = self.fixtures.filter(fixture_date__gte=datetime.today())
        fixtures_ordered = fixtures_on_or_after_today.order_by('fixture_date')
        next_fixtures = fixtures_ordered[:6]
        return next_fixtures



    def display_name(self):
        return self.title

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()