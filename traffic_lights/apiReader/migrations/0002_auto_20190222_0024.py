# Generated by Django 2.1.7 on 2019-02-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiReader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='', max_length=500),
        ),
    ]
