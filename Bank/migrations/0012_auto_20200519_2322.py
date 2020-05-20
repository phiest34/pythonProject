# Generated by Django 3.0.4 on 2020-05-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0011_auto_20200519_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank_b',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bank_s',
            name='id',
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='ADR',
            field=models.CharField(default='0', max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='BIC',
            field=models.CharField(default='0', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='DT',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='NAME_B',
            field=models.CharField(default='0', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='OGRN',
            field=models.CharField(default='0', max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='OKATO',
            field=models.CharField(default='0', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='OKPO',
            field=models.CharField(default='0', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='REGN',
            field=models.CharField(default='0', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bank_b',
            name='REGN_S',
            field=models.CharField(default='0', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='bank_s',
            name='C1_S',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bank_s',
            name='C2_S',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bank_s',
            name='C31_S',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bank_s',
            name='C32_S',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bank_s',
            name='REGN',
            field=models.CharField(default='0', max_length=10, primary_key=True, serialize=False),
        ),
    ]
