# Generated by Django 3.1.1 on 2020-09-19 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='opinions.question'),
        ),
    ]
