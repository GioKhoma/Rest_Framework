# Generated by Django 5.0.6 on 2024-07-08 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0010_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('pending_status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='PAYMENT_STATUS_PENDING', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='storeapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storeapp.product')),
            ],
        ),
    ]
