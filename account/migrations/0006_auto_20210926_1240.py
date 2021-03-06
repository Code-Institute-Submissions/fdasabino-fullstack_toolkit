# Generated by Django 3.1.4 on 2021-09-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_userbase_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='address_line_1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='userbase',
            old_name='address_line_2',
            new_name='address2',
        ),
        migrations.RenameField(
            model_name='userbase',
            old_name='town_city',
            new_name='city',
        ),
        migrations.AlterField(
            model_name='userbase',
            name='country',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
