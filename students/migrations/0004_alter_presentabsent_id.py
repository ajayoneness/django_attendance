# Generated by Django 4.0.3 on 2022-04-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_presentabsent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentabsent',
            name='id',
            field=models.TextField(max_length=250, primary_key=True, serialize=False),
        ),
    ]
