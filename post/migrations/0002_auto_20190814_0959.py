# Generated by Django 2.2.4 on 2019-08-14 01:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
