# Generated by Django 3.2.4 on 2021-09-27 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210926_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
