# Generated by Django 3.2 on 2022-04-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='lid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
