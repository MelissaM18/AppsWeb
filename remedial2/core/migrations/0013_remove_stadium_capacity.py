# Generated by Django 4.2.7 on 2023-12-05 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_stadium_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stadium',
            name='capacity',
        ),
    ]
