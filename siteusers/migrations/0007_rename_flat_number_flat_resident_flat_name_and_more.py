# Generated by Django 4.2.7 on 2024-03-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteusers', '0006_caretakerapproval_order_caretaker_approval'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat_resident',
            old_name='flat_number',
            new_name='flat_name',
        ),
        migrations.RemoveField(
            model_name='flat_resident',
            name='caretaker_approved',
        ),
        migrations.AddField(
            model_name='flat_resident',
            name='caretaker_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
