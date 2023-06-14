from django.db import models

# Create your models here.


class effects(models.IntegerChoices):
    off = 0, 'Off'
    rainbowFade = 1, 'Rainbow Fade'
    fire = 2, 'Fire'
    spectrum = 3, 'Spectrum'
    heartBeat = 4, 'Heart Beat'


class status(models.Model):
    status = models.IntegerField(choices=effects.choices, default=effects.off)
