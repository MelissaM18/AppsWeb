# Generated by Django 4.2.7 on 2023-12-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_player_number_alter_stadium_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stadium',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
