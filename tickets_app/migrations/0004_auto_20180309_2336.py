# Generated by Django 2.0.3 on 2018-03-09 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tickets_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_app', '0003_auto_20180309_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(default=tickets_app.models.author, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]