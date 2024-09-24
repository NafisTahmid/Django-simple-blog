# Generated by Django 5.1.1 on 2024-09-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('featured_image', models.ImageField(upload_to='uploads/')),
                ('tags', models.CharField(max_length=50)),
                ('featured', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
