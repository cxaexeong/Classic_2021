
# Generated by Django 3.2.5 on 2021-07-30 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(

            name='Clothes_Main_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField()),
                ('month', models.IntegerField()),
                ('image', models.ImageField(upload_to='clothing/images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.color')),
                ('length', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.length')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes_main_type')),

            ],
        ),
    ]
