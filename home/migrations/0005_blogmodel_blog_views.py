# Generated by Django 3.2.5 on 2021-07-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
    ]
