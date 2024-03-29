# Generated by Django 4.0.1 on 2022-03-25 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_listing_category_alter_listing_post_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Jobs', 'Jobs'), ('Furniture', 'Furniture'), ('Fashion', 'Fashion'), ('Property', 'Property'), ('Electronics', 'Electronics'), ('Books&Sports', 'Books&Sports'), ('Mobiles', 'Mobiles'), ('Bikes', 'Bikes'), ('Cars', 'Cars')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 26, 3, 37, 35, 99497)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('UP', 'Uttar Pradesh'), ('GJ', 'Gujarat'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('TR', 'Tripura'), ('PB', 'Punjab'), ('MH', 'Maharashtra'), ('WB', 'West Bengal'), ('ML', 'Meghalaya'), ('TN', 'Tamil Nadu'), ('GA', 'Goa'), ('OD', 'Odisha'), ('TS', 'Telegana'), ('KA', 'Karnataka'), ('RJ', 'Rajasthan'), ('MZ', 'Mizoram'), ('AR', 'Arunachal Pradesh'), ('JH', 'Jharkhand'), ('UK', 'Uttarakhand'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('HP', 'Haryana'), ('AS', 'Assam'), ('NL', 'Nagaland'), ('AP', 'Andhra Pradesh'), ('MI', 'Sikkim'), ('KL', 'Kerala')], max_length=100),
        ),
    ]
