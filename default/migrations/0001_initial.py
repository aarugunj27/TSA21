# Generated by Django 3.2.8 on 2021-10-28 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('email', models.CharField(max_length=64)),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]
