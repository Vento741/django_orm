# Generated by Django 5.0.6 on 2024-05-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('image', models.URLField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(allow_unicode=True, blank=True)),
            ],
        ),
    ]
