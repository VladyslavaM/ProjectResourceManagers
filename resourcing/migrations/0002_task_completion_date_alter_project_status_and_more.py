# Generated by Django 4.2.6 on 2023-11-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='To Do', max_length=20),
        ),
    ]
