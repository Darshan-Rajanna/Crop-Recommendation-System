# Generated by Django 5.0.1 on 2024-07-21 19:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recomender', '0002_crophistory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crophistory',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]