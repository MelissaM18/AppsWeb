# Generated by Django 4.2.7 on 2023-12-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_stadium_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadium',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
    ]
