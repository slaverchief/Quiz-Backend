from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['quiz__name', 'content']

admin.site.register(Quiz)


