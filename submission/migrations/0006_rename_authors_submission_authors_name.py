# Generated by Django 4.1 on 2022-11-01 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0005_submission_track'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='authors',
            new_name='authors_name',
        ),
    ]
