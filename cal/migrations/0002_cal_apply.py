# Generated by Django 2.2.3 on 2019-07-15 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cal',
            name='apply',
            field=models.TextField(null=True),
        ),
    ]
