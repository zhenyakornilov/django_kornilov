# Generated by Django 3.2.5 on 2021-10-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20210911_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-id']},
        ),
    ]