# Generated by Django 3.2.4 on 2021-06-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keterangan', '0002_peta'),
    ]

    operations = [
        migrations.AddField(
            model_name='peta',
            name='thumb',
            field=models.ImageField(blank=True, default='defaul.png', upload_to=''),
        ),
    ]
