# Generated by Django 4.2.1 on 2023-06-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dress_effects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Off'), (1, 'Rainbow Fade'), (2, 'Fire'), (3, 'Spectrum'), (4, 'Heart Beat')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='fire_effects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='untitled', max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Off'), (1, 'on')], default=0)),
            ],
        ),
    ]
