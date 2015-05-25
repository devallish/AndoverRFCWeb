from django.db import models
from datetime import datetime, date
from helpers import site_utils


def get_news_image_filename(instance, uploaded_filename):
    return site_utils.create_file_name('news', instance.id, uploaded_filename)


class NewsArticle(models.Model):
    headline = models.CharField(max_length=50)
    summary = models.TextField(null=True, blank=True)
    full_story = models.TextField()
    news_image = models.ImageField(upload_to=get_news_image_filename, null=True, blank=True)
    news_date = models.DateTimeField(default=datetime.now())
    publish_date = models.DateField(default=date.today())
    remove_date = models.DateField(null=True, blank=True)

    def display_name(self):
        return self.news_date.strftime('%a %d %b %Y') + ' - ' + self.headline

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()