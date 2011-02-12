from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Voicemail(models.Model):
    EVENT_CHOICES = (
        ('H', 'Hurricane'),
        ('E', 'Earthquake'),
    )

    URGENCY_CHOICES = (
        ('C', 'Chilling'),
        ('S', 'Spam'),
    )

    user            = models.ForeignKey(User, blank=True)

    audio_file      = models.URLField()
    phone_number    = models.CharField( max_length= 15 )
    date            = models.DateTimeField(auto_now=True)
    transcription   = models.TextField( blank=True )
    call_summary    = models.CharField( max_length = 255, blank=True)
    location        = models.CharField( max_length = 255, blank=True)
    event           = models.CharField( max_length = 10, choices=EVENT_CHOICES , blank=True)
    urgency         = models.CharField( max_length = 10,
choices=URGENCY_CHOICES, blank=True)
    tags            = models.CharField( max_length = 255, blank=True)
    need            = models.TextField(blank=True)
    last_saved      = models.DateTimeField(auto_now = True, blank=True)
    reviewed        = models.BooleanField(blank=True)

    def __str__(self):
        return self.phone_number + " on " + self.date.isoformat()

