# Generated by Django 4.2.19 on 2025-02-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(blank=True)),
            ],
        ),
    ]
