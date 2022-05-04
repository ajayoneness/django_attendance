from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='presentabsent',
            fields=[
                ('date', models.DateField()),
                ('enrollment', models.TextField(max_length=200)),
                ('sub', models.TextField(max_length=100)),
                ('sem', models.TextField(max_length=100)),
                ('teacher', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('name', models.TextField(max_length=200)),
                ('enrollment_no', models.TextField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),

        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.TextField(max_length=200)),
                ('subject', models.TextField(max_length=200)),
                ('sem', models.TextField(max_length=100)),
            ],
        ),
    ]
