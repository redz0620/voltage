# Generated by Django 4.0.5 on 2022-06-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_admin_update_contact_message_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
