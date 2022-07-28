# Generated by Django 4.0.4 on 2022-07-26 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_category_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='listing',
        ),
        migrations.AddField(
            model_name='auctionslisting',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.category'),
        ),
    ]