from django.contrib import admin

from .models import Question, Choice, Course

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Course)
