from django.db import models
from django.utils import timezone


class Store(models.Model):
    """店舗情報"""

    name = models.CharField('店舗名', max_length=255)
    is_wifi = models.BooleanField('WiFi利用有無', default=False)
    address = models.CharField('住所', max_length=255)
    tel = models.CharField('電話番号', max_length=255)
    open_time = models.CharField('営業時間', max_length=255)
    latitude = models.CharField('緯度', max_length=255)
    longitude = models.CharField('経度', max_length=255)
    hotPepper_id = models.CharField('HotPepperId', max_length=255)
    registedDate_at = models.DateTimeField('登録日', default=timezone.now)

    def __str__(self):
        return self.name
