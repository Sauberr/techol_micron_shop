# Generated by Django 4.2 on 2024-03-19 18:05

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0012_alter_profile_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
