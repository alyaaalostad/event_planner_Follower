# Generated by Django 2.2.5 on 2019-09-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190908_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.PositiveIntegerField(default=50),
            preserve_default=False,
        ),
    ]
