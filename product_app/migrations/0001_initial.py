# Generated by Django 4.2.2 on 2023-06-23 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='product_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=200)),
                ('Quality', models.IntegerField()),
                ('price', models.ImageField(upload_to='')),
                ('manufacture_date', models.DateField(auto_now_add=True)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.category')),
            ],
        ),
    ]