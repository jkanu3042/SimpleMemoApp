from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.

class Memo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(verbose_name='내용')

    photo = models.ImageField(blank=True, upload_to='post/memo/%Y/%m/%d')
    photo_thumbnail = ImageSpecField(
                            source='photo',
                            processors=[Thumbnail(100, 50)],
                            format='JPEG',
                            options={'quality': 60})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:memo_detail', args=[self.pk])

