# Generated by Django 4.0.7 on 2022-12-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0002_blogdata_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='img',
            field=models.URLField(max_length=20000, null=True),
        ),
    ]