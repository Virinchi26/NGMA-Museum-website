# Generated by Django 4.1.3 on 2022-11-24 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NGMAapp', '0004_remove_transaction_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='datetime_of_payment',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='transaction',
            name='order_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILURE'), (3, 'PENDING')], default=3),
        ),
        migrations.AddField(
            model_name='transaction',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='States',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='zipcode',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
