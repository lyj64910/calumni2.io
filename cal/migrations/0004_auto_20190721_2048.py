# Generated by Django 2.2.3 on 2019-07-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20190715_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cal',
            name='com',
        ),
        migrations.AddField(
            model_name='cal',
            name='act',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cal',
            name='schoolact',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cal',
            name='score',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cal',
            name='write',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cal',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
