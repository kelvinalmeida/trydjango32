# Generated by Django 3.2.23 on 2023-11-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='content',
            field=models.TextField(default='new content'),
            preserve_default=False,
        ),
    ]