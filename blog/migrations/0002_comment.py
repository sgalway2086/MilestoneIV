# Generated by Django 3.2.9 on 2021-12-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=254)),
                ('comment_body', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.CharField(max_length=80)),
            ],
        ),
    ]
