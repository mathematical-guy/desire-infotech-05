# Generated by Django 3.2 on 2024-06-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[['Action', 'ACTION'], ['Fiction', 'Fiction'], ['Horror', 'Horror'], ['Comedy', 'COMEDY']], max_length=30),
        ),
    ]