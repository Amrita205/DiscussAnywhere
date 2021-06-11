# Generated by Django 3.2 on 2021-06-02 18:00

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='latests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=100)),
                ('desc1', models.CharField(max_length=100)),
                ('desc2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phno', models.IntegerField()),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, default='image/defaultprofile.jpg', null=True, upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('post_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.post')),
            ],
        ),
    ]
