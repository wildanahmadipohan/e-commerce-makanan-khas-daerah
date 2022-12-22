# Generated by Django 3.2 on 2022-02-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220215_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='province_id',
        ),
        migrations.RemoveField(
            model_name='store',
            name='regency_id',
        ),
        migrations.AddField(
            model_name='store',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]