# Generated by Django 3.2.4 on 2021-09-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_userbase_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
