# Generated by Django 3.2.11 on 2024-04-26 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_firtsname_approvals_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvals',
            old_name='coapplicantincome',
            new_name='coapplicatincome',
        ),
    ]
