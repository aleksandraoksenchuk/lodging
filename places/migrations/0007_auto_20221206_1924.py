# Generated by Django 3.2.16 on 2022-12-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_remove_booking_продолжительность'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='first_day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='passport',
            field=models.CharField(max_length=9),
        ),
    ]
