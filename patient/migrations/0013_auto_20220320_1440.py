# Generated by Django 3.2.9 on 2022-03-20 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_rename_service_booking_selectservice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='appointment_date',
            new_name='appointmentdate',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='appointment_time',
            new_name='appointmenttime',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='special_request',
            new_name='specialrequest',
        ),
    ]
