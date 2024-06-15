# Generated by Django 4.2.4 on 2024-06-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('owner_name', models.CharField(max_length=300)),
                ('expiry_date', models.DateField()),
                ('cvv', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=30)),
            ],
        ),
    ]