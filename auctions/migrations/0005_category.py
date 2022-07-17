# Generated by Django 4.0.5 on 2022-07-17 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_auctionslisting_user_id_auctionslisting_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('auction', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.auctionslisting')),
            ],
        ),
    ]
