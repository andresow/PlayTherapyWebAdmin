# Generated by Django 2.2.5 on 2019-10-01 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20190930_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='list_diagnostic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Diagnostic', unique=True),
        ),
    ]
