from django.db import models
from news.models import NewsArticle


class Event(models.Model):
    name = models.CharField(max_length=50)
    information = models.TextField()
    event_date = models.DateTimeField()
    use_event_time = models.BooleanField(default=False)
    news_article = models.OneToOneField(NewsArticle, null=True, blank=True)

    def display_details(self):
        if self.use_event_time:
            message = self.event_date.strftime('%a %d %b %Y - %H:%M')
        else:
            message = self.event_date.strftime('%a %d %b %Y')
        return message

    def display_heading(self):
        return self.name

    def display_name(self):
        return self.event_date.strftime('%a %d %b %Y') + ' - ' + self.name

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()