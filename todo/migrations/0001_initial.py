# Generated by Django 3.0.5 on 2020-08-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
