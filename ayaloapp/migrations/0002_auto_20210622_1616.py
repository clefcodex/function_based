# Generated by Django 3.2.4 on 2021-06-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayaloapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='AccountType',
            field=models.CharField(choices=[(1, 'Leeser'), (2, 'leesee')], max_length=2),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]