# Generated by Django 3.2.5 on 2021-09-08 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_curator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='group_monitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]
