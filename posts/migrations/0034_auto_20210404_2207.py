# Generated by Django 2.2 on 2021-04-04 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_comment_editor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['first_name']},
        ),
        migrations.RemoveField(
            model_name='image',
            name='comment',
        ),
    ]