# Generated by Django 4.1.4 on 2022-12-24 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtributeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(default='', max_length=200)),
                ('kod', models.CharField(default='', max_length=200)),
                ('zobrazit', models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hodnota', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hodnota_atributu_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.attributevalue')),
                ('nazev_atributu_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.atributename')),
            ],
        ),
    ]
