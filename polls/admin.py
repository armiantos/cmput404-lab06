from django.contrib import admin

from polls.models import Choice, Question

admin.site.register(Choice)
admin.site.register(Question)
