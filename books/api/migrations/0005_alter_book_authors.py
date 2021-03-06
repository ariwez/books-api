# Generated by Django 3.2.5 on 2021-07-04 10:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_book_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, default=list, null=True, size=None),
        ),
    ]
