# Generated by Django 3.2 on 2021-05-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img/%y')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
