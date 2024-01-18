# Generated by Django 4.1.5 on 2023-01-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_pereval_areas_id_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.AddField(
            model_name='users',
            name='fam',
            field=models.TextField(max_length=15, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.TextField(max_length=15, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='users',
            name='otc',
            field=models.TextField(max_length=15, null=True, verbose_name='Отчество'),
        ),
    ]