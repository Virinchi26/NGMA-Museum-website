# Generated by Django 4.1.3 on 2022-11-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGMAapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Total_Amount',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
