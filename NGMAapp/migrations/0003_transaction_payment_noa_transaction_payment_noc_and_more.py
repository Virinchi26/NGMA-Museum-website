# Generated by Django 4.1.3 on 2022-11-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGMAapp', '0002_transaction_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Payment_NoA',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Payment_NoC',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Payment',
            field=models.CharField(max_length=122),
        ),
    ]
