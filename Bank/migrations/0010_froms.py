# Generated by Django 3.0.4 on 2020-06-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Bank', '0009_auto_20200605_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='froms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(default='0', max_length=100, null=True)),
            ],
        ),
    ]
