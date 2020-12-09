# Generated by Django 3.0 on 2020-02-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(choices=[('MALINDI', 'Malindi'), ('WATAMU', 'Watamu')], default='MALINDI', max_length=20),
        ),
    ]
