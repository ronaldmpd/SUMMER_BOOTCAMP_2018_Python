# Generated by Django 2.0.2 on 2018-02-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
    ]
