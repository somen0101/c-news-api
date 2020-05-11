# Generated by Django 2.2.5 on 2020-05-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_topics_sentimental'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(null=True)),
                ('title', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('published_date', models.TextField(null=True)),
                ('author', models.TextField(null=True)),
                ('topic_url', models.TextField(null=True)),
                ('image_url', models.TextField(null=True)),
                ('sentimental', models.TextField(null=True)),
            ],
        ),
    ]