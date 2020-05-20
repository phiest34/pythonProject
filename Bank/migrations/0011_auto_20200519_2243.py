# Generated by Django 3.0.4 on 2020-05-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0010_auto_20200519_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_b',
            name='DT',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='bank_b',
            name='REGN',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='bank_s',
            name='REGN',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='ADR',
            field=models.CharField(default='0', max_length=130),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='BIC',
            field=models.CharField(default='0', max_length=9),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='NAME_B',
            field=models.CharField(default='0', max_length=60),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='OGRN',
            field=models.CharField(default='0', max_length=13),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='OKATO',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='OKPO',
            field=models.CharField(default='0', max_length=8),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='REGN_S',
            field=models.CharField(default='0', max_length=3),
        ),
    ]
