# Generated by Django 4.0.3 on 2022-04-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentabsent',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
