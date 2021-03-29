# Generated by Django 3.1.7 on 2021-03-28 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dis_likes', to='posts.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('caption', models.TextField()),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.comment')),
                ('dislikes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.dislike')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('bio', models.TextField()),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='like',
            name='users',
            field=models.ManyToManyField(related_name='requirement_comment_likes', to='posts.Profile'),
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.like'),
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.profile'),
        ),
        migrations.AddField(
            model_name='dislike',
            name='users',
            field=models.ManyToManyField(related_name='requirement_comment_dis_likes', to='posts.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.profile'),
        ),
    ]
