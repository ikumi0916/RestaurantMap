# Generated by Django 3.2 on 2021-05-03 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='店舗名')),
                ('is_wifi', models.BooleanField(default=False, verbose_name='WiFi利用有無')),
                ('address', models.CharField(max_length=255, verbose_name='住所')),
                ('tel', models.CharField(max_length=255, verbose_name='電話番号')),
                ('open_time', models.CharField(max_length=255, verbose_name='営業時間')),
                ('latitude', models.CharField(max_length=255, verbose_name='緯度')),
                ('longitude', models.CharField(max_length=255, verbose_name='経度')),
                ('hotPepper_id', models.CharField(max_length=255, verbose_name='HotPepperId')),
                ('registedDate_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
            ],
        ),
    ]
