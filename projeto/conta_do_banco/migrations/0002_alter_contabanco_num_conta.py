# Generated by Django 4.1 on 2022-08-03 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta_do_banco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contabanco',
            name='num_conta',
            field=models.IntegerField(),
        ),
    ]