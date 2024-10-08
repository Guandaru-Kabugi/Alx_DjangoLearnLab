# Generated by Django 5.1 on 2024-09-13 08:17

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_slug'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
