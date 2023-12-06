# Generated by Django 4.2.7 on 2023-12-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_team_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='stadium',
            name='city',
            field=models.CharField(default='Nombre de la Ciudad', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='venue',
            field=models.CharField(default='Nombre de la Ciudad de Origen', max_length=100),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]