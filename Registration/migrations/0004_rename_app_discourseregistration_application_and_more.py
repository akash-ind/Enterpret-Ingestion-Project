# Generated by Django 4.1.5 on 2023-02-06 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_discourseregistration_access_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discourseregistration',
            old_name='app',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='intercomregistration',
            old_name='app',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='playstoreregistration',
            old_name='app',
            new_name='application',
        ),
        migrations.RenameField(
            model_name='twitterregistration',
            old_name='app',
            new_name='application',
        ),
    ]
