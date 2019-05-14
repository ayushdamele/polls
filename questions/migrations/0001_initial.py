# Generated by Django 2.2.1 on 2019-05-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=30)),
                ('opt1', models.CharField(max_length=30)),
                ('opt2', models.CharField(max_length=30)),
                ('opt3', models.CharField(max_length=30)),
                ('opt4', models.CharField(max_length=30)),
                ('vot1', models.IntegerField(default=0)),
                ('vot2', models.IntegerField(default=0)),
                ('vot3', models.IntegerField(default=0)),
                ('vot4', models.IntegerField(default=0)),
            ],
        ),
    ]
