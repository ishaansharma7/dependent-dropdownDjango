# Generated by Django 3.1.7 on 2021-04-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_auto_20210413_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
