# Generated by Django 3.2 on 2021-05-18 14:20

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='name',
            new_name='tittle',
        ),
        migrations.RemoveField(
            model_name='art',
            name='image',
        ),
        migrations.AddField(
            model_name='art',
            name='post_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='art',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
