# Generated by Django 4.1.7 on 2023-03-25 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acornmoodtracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeling',
            old_name='parentMoodID',
            new_name='moodID',
        ),
    ]
