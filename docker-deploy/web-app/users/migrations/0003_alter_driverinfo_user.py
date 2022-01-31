# Generated by Django 4.0.1 on 2022-01-28 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driverinfo', to=settings.AUTH_USER_MODEL),
        ),
    ]
