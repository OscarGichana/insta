# Generated by Django 2.2 on 2021-03-30 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20210330_1139'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]