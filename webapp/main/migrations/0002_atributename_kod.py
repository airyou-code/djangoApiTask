# Generated by Django 4.1.4 on 2022-12-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atributename',
            name='kod',
            field=models.CharField(default='', max_length=200),
        ),
    ]
