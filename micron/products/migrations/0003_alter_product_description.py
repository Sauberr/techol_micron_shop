# Generated by Django 4.2 on 2024-02-03 16:20

from django_ckeditor_5.fields import CKEditor5Field
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=CKEditor5Field(config_name='extends', blank=True, null=True),
        ),
    ]
