# Generated by Django 4.0.2 on 2022-02-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Number_of_Buisness', models.IntegerField()),
            ],
        ),
    ]
