# Generated by Django 4.0.5 on 2022-07-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_shopcart_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='name_id',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
