# Generated by Django 3.2.4 on 2021-06-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keterangan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
            ],
        ),
    ]
