# Generated by Django 3.2.5 on 2021-09-09 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_monitor',
            field=models.ForeignKey(db_column='Group monitor', null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]