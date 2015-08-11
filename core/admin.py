from django.contrib import admin

# Register your models here.

from .models import Survey, Question, Answer, Response

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Response)