# Generated by Django 4.1.2 on 2022-12-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopkeeper',
            name='companyname',
            field=models.CharField(max_length=256),
        ),
    ]