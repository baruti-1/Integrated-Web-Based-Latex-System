# Generated by Django 3.2 on 2021-07-07 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0006_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportformatstudent',
            old_name='student',
            new_name='uploaded_by',
        ),
    ]
