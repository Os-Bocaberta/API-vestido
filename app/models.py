from django.db import models

# Create your models here.


class dress_options(models.IntegerChoices):
    off = 0, 'Off'
    rainbowFade = 1, 'Rainbow Fade'
    fire = 2, 'Fire'
    spectrum = 3, 'Spectrum'
    heartBeat = 4, 'Heart Beat'


class fire_options(models.IntegerChoices):
    off = 0, 'Off'
    on = 1, 'on'


class dress_effects(models.Model):
    status = models.IntegerField(
        choices=dress_options.choices, default=dress_options.off)


class fire_effects(models.Model):
    name = models.CharField(default='untitled', max_length=255)
    status = models.IntegerField(choices=fire_options.choices, default=fire_options.off)
