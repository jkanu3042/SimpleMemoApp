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
                            processors=[Thumbnail(300, 300)],
                            format='JPEG',
                            options={'quality': 60})
    tag_set = models.ManyToManyField('Tag', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:memo_detail', args=[self.pk])

    class Meta:
        ordering =['-id']

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL) #user
    post = models.ForeignKey(Memo) #post_id 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message