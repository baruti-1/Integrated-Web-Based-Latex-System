# Generated by Django 3.2 on 2021-07-07 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0008_rename_uploaded_by_reportformatstudent_uploader'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportformatstudent',
            old_name='uploader',
            new_name='uploaded_by',
        ),
    ]