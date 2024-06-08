# Generated by Django 4.2.9 on 2024-06-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_attendance_month_attendance_overtime_attendance_year_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name_plural': 'attendance records'},
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='Attendance_id',
            new_name='attendance_id',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='Employee',
            new_name='employee',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='Month',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='Overtime',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='Year',
        ),
        migrations.AlterModelTable(
            name='attendance',
            table='attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='overtime',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]