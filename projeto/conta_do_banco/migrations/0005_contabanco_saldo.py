# Generated by Django 4.1 on 2022-08-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta_do_banco', '0004_remove_contabanco_deposito'),
    ]

    operations = [
        migrations.AddField(
            model_name='contabanco',
            name='saldo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]