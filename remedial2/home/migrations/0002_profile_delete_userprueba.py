# Generated by Django 4.2.7 on 2023-12-05 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='User Axolotl', max_length=32, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(blank=True, default='user@gmail.com', max_length=254, null=True)),
                ('bio', models.CharField(blank=True, default='AXOLOTL FURNITURE', max_length=256, null=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserPrueba',
        ),
    ]
