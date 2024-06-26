# Generated by Django 4.2.7 on 2024-03-10 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteusers', '0007_rename_flat_number_flat_resident_flat_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=16)),
                ('expiration_date', models.CharField(max_length=7)),
                ('cvv', models.CharField(max_length=3)),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteusers.payment'),
        ),
    ]
