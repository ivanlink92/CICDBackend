# Generated by Django 5.1.7 on 2025-03-13 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_item_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='title',
        ),
    ]
