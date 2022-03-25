# Generated by Django 4.0.1 on 2022-03-25 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_alter_listing_category_alter_listing_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Jobs', 'Jobs'), ('Property', 'Property'), ('Fashion', 'Fashion'), ('Cars', 'Cars'), ('Bikes', 'Bikes'), ('Furniture', 'Furniture'), ('Books&Sports', 'Books&Sports'), ('Electronics', 'Electronics')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='listing',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 26, 4, 23, 47, 811493)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('HP', 'Haryana'), ('TS', 'Telegana'), ('JH', 'Jharkhand'), ('KL', 'Kerala'), ('BR', 'Bihar'), ('TR', 'Tripura'), ('OD', 'Odisha'), ('GA', 'Goa'), ('UK', 'Uttarakhand'), ('KA', 'Karnataka'), ('TN', 'Tamil Nadu'), ('ML', 'Meghalaya'), ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'), ('AR', 'Arunachal Pradesh'), ('GJ', 'Gujarat'), ('MN', 'Manipur'), ('PB', 'Punjab'), ('MI', 'Sikkim'), ('MZ', 'Mizoram'), ('AP', 'Andhra Pradesh'), ('RJ', 'Rajasthan'), ('MP', 'Madhya Pradesh'), ('CG', 'Chhattisgarh'), ('AS', 'Assam'), ('WB', 'West Bengal'), ('NL', 'Nagaland')], max_length=100),
        ),
    ]
