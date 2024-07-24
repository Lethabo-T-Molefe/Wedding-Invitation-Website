# Generated by Django 5.0.7 on 2024-07-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=15)),
                ('church_attendence', models.BooleanField()),
                ('home_attendence', models.BooleanField()),
                ('song_request', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
