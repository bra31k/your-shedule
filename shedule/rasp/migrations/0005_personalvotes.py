# Generated by Django 2.0.4 on 2018-05-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0004_weekendsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('selected_day', models.CharField(max_length=7)),
            ],
        ),
    ]
