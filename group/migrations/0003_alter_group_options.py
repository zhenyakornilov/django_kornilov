# Generated by Django 3.2.5 on 2021-10-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_group_group_monitor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['id']},
        ),
    ]