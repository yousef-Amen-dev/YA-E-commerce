# Generated by Django 5.0.7 on 2024-08-19 17:39

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0019_customer_adderss'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/users_profile_images/')),
                ('adderss1', models.CharField(blank=True, default=None, max_length=400, null=True, verbose_name='Address')),
                ('adderss2', models.CharField(blank=True, default=None, max_length=400, null=True, verbose_name='Address')),
                ('phone', models.CharField(blank=True, default=None, max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(11, 'The Field Must be contain 11 Numbers')])),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('zipcode', models.CharField(blank=True, max_length=200)),
                ('countery', models.CharField(blank=True, max_length=200)),
                ('joined_at', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]