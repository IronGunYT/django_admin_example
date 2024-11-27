# Generated by Django 5.0.6 on 2024-11-27 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('pages', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='core.author')),
            ],
        ),
    ]
