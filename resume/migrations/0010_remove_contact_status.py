# Generated by Django 4.1.5 on 2023-02-17 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_contact_r_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='status',
        ),
    ]
