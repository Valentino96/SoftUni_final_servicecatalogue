# Generated by Django 4.1.3 on 2022-12-12 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecomment',
            name='service',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='common.service'),
        ),
    ]
