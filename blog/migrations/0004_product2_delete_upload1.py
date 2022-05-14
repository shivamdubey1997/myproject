# Generated by Django 4.0.3 on 2022-04-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_upload1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_category', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_date', models.DateField()),
                ('product_image', models.ImageField(default='', upload_to='blog/image')),
            ],
        ),
        migrations.DeleteModel(
            name='upload1',
        ),
    ]
