# Generated by Django 3.0.7 on 2020-06-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200625_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
