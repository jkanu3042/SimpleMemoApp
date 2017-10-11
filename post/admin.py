from django.contrib import admin
from .models import Memo
# Register your models here.

@admin.register(Memo)
class PostAdmin(admin.ModelAdmin):
    pass