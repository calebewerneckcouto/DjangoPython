# Generated by Django 5.1.4 on 2025-01-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
