# Generated by Django 2.0.5 on 2020-03-16 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petclinic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='food',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='hungry',
        ),
    ]
