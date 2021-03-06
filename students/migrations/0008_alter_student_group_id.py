# Generated by Django 3.2.5 on 2021-09-11 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_group_group_monitor'),
        ('students', '0007_rename_group_name_student_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group_id',
            field=models.ForeignKey(db_column='Group ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='group.group'),
        ),
    ]
