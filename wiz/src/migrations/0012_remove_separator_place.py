# Generated by Django 4.0.2 on 2022-07-15 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0011_remove_employer_facebook_remove_employer_instagram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='separator',
            name='place',
        ),
    ]
