# Generated by Django 3.2.15 on 2022-09-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patronupgrade',
            name='order_number',
            field=models.CharField(default=12345678904364576, editable=False, max_length=32),
            preserve_default=False,
        ),
    ]
