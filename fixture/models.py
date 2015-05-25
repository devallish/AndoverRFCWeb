from django.db import models
import datetime


class Fixture(models.Model):

    NINE_AM = datetime.time(hour=9)
    NINE_THIRTY_AM = datetime.time(hour=9, minute=30)
    TEN_AM = datetime.time(hour=10)
    TEN_THIRTY_AM = datetime.time(hour=10, minute=30)
    ELEVEN_AM = datetime.time(hour=11)
    ELEVEN_THIRTY_AM = datetime.time(hour=11, minute=30)
    TWELVE_PM = datetime.time(hour=12)
    TWELVE_THIRTY_PM = datetime.time(hour=12, minute=30)
    ONE_PM = datetime.time(hour=13)
    ONE_THIRTY_PM = datetime.time(hour=13, minute=30)
    TWO_PM = datetime.time(hour=14)
    TWO_THIRTY_PM = datetime.time(hour=14, minute=30)
    THREE_PM = datetime.time(hour=15)

    TIME_OPTIONS = (
        (NINE_AM, '9:00 AM'),
        (TEN_AM, '10:00 AM'),
        (TEN_THIRTY_AM, '10:30 AM'),
        (ELEVEN_AM, '11:00 AM'),
        (ELEVEN_THIRTY_AM, '11:30 AM'),
        (TWELVE_PM, 'Midday'),
        (TWELVE_THIRTY_PM, '12:30 PM'),
        (ONE_PM, '1:00 PM'),
        (ONE_THIRTY_PM, '1:30 PM'),
        (TWO_PM, '2:00 PM'),
        (TWO_THIRTY_PM, '2:30 PM'),
        (THREE_PM, '3:00 PM')
    )

    opposition = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    fixture_date = models.DateField()
    meet_time = models.TimeField(choices=TIME_OPTIONS, null=True, blank=True)
    kick_off_time = models.TimeField(choices=TIME_OPTIONS)
    # kick_off_time = models.TimeField()
    doofa = models.CharField(max_length=50, null=True, blank=True)
    dress_code = models.CharField(max_length=50, null=True, blank=True)

    def display_details(self):
        message = self.fixture_date.strftime('%a %d %b %Y ') + ' - KO: ' + self.kick_off_time.strftime('%H:%M')
        return message

    def display_heading(self):
        if self.squad_set.count() > 0:
            squad = self.squad_set.get()
            message = squad.name
        else:
            message = "Andover"
        message += ' v ' + self.opposition
        message += ' @ ' + self.venue
        return message

    def display_name(self):
        return self.fixture_date.strftime('%a %d %b %Y') + ' - ' + self.opposition

    def __unicode__(self):
        return self.display_name()

    def __str__(self):
        return self.display_name()