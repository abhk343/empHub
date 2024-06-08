# Generated by Django 4.2.9 on 2024-06-06 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_attendance_options_remove_attendance_overtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DOL',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Overtime', models.IntegerField()),
                ('Date', models.DateField()),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'db_table': 'Overtime',
            },
        ),
    ]