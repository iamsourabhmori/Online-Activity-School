# Generated by Django 3.1.6 on 2023-06-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('courseid', models.AutoField(primary_key=True, serialize=False)),
                ('nm', models.CharField(max_length=25)),
                ('duration', models.IntegerField()),
                ('fees', models.IntegerField()),
                ('coursedetails', models.CharField(max_length=200)),
                ('courseicon', models.CharField(max_length=60)),
            ],
        ),
    ]
