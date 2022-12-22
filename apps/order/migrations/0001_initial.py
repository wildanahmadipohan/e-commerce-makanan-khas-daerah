# Generated by Django 3.2 on 2022-02-23 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_alter_product_price'),
        ('store', '0005_remove_store_postal_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('regency', models.CharField(max_length=100)),
                ('paid_amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_proof', models.ImageField(blank=True, null=True, upload_to='uploads/payment')),
                ('user_paid', models.BooleanField(default=False)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='store.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='product.product')),
            ],
        ),
    ]