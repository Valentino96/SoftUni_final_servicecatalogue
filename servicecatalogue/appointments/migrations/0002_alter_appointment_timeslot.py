# Generated by Django 4.1.3 on 2022-12-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeslot',
            field=models.IntegerField(choices=[(0, '10'), (1, '11'), (2, '12'), (3, '13'), (4, '14'), (5, '15'), (6, '16'), (7, '17'), (8, '18')]),
        ),
    ]
