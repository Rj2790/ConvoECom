# Generated by Django 3.2.3 on 2021-11-16 07:27

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
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='Ecom/categories')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(blank=True, default=False, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200, null=True)),
                ('last_name', models.CharField(default='', max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ecom.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('regular_price', models.IntegerField(blank=True, default=0)),
                ('sale_price', models.IntegerField(blank=True, default=0)),
                ('short_description', models.TextField()),
                ('product_detail', models.TextField()),
                ('publish_date', models.DateField()),
                ('image1', models.ImageField(upload_to='Ecom/images')),
                ('image2', models.ImageField(blank=True, upload_to='Ecom/images')),
                ('image3', models.ImageField(blank=True, upload_to='Ecom/images')),
                ('image4', models.ImageField(blank=True, upload_to='Ecom/images')),
                ('category', models.ManyToManyField(related_name='prod_category', to='Ecom.Categories')),
                ('variant', models.ManyToManyField(default=None, related_name='prod_variant', to='Ecom.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ecom.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ecom.product')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ecom.variant')),
            ],
        ),
    ]
