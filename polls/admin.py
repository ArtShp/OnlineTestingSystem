from django.contrib import admin
from .models import Quiz, Question, Answer

'''
class PersonAdmin(admin.ModelAdmin):
    list_display = ['question.content']
'''

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
