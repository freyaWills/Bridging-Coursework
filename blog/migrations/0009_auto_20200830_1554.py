# Generated by Django 2.2.14 on 2020-08-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200830_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
