# Generated by Django 4.1 on 2022-10-28 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='decison',
            new_name='decision',
        ),
    ]
