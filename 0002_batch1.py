# Generated by Django 3.1.6 on 2023-06-27 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='batch1',
            fields=[
                ('batchid', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField()),
                ('batchtime', models.CharField(max_length=30)),
                ('facultyname', models.CharField(max_length=40)),
                ('batchstatus', models.IntegerField()),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course')),
            ],
        ),
    ]