# Generated by Django 2.2 on 2021-03-30 08:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0012_auto_20210330_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
