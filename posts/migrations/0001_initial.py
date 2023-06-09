# Generated by Django 4.1.2 on 2023-03-21 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('name', models.CharField(db_index=True, max_length=14, verbose_name='Name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('random_num', models.AutoField(primary_key=True, serialize=False, verbose_name='Random Number')),
                ('Student_class', models.CharField(max_length=12, verbose_name='Class')),
                ('section', models.CharField(max_length=12, verbose_name='Section')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
