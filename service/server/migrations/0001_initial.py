# Generated by Django 2.1.7 on 2019-04-09 07:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
