# Generated by Django 3.2 on 2021-06-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20210602_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='topic',
            field=models.CharField(max_length=200, null=True),
        ),
    ]