# Generated by Django 3.2.5 on 2021-09-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20210908_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(db_column='Group name', max_length=200, verbose_name='Group Name'),
        ),
    ]
