# Generated by Django 3.2.9 on 2022-03-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20220319_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='appointmentdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='appointmenttime',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
