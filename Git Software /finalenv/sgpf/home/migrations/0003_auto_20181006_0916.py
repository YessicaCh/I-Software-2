# Generated by Django 2.1 on 2018-10-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_concept_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='isFixed',
        ),
        migrations.AlterField(
            model_name='concept',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
