from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Memo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(verbose_name='내용')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


