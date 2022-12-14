# Generated by Django 4.1 on 2022-08-21 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCardPropType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=400)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('ide', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ICategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idc', models.IntegerField()),
                ('slug', models.TextField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('imageUrl', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='IProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idp', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('slug', models.TextField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('imageUrl', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('startDate', models.CharField(max_length=200)),
                ('endDate', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('noOfSeats', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
                ('categoryId', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.icategory')),
            ],
        ),
    ]
