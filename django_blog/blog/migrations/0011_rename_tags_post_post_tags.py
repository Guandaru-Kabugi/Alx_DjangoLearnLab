# Generated by Django 5.1 on 2024-09-13 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_tags_post_tags_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags_post',
            new_name='tags',
        ),
    ]
