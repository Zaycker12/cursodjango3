# Generated by Django 3.1.3 on 2020-11-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]