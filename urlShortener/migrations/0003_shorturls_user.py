# Generated by Django 4.1.1 on 2022-09-06 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urlShortener', '0002_shorturls_expiration_day_shorturls_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturls',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
