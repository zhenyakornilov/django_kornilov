# Generated by Django 3.2.5 on 2021-10-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['id']},
        ),
    ]
