# Generated by Django 5.0 on 2023-12-25 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Category',
            new_name='category',
        ),
    ]
