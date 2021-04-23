from django.contrib import admin
from .models import Quiz, Question, Answer, AnsweredQuiz

'''
class PersonAdmin(admin.ModelAdmin):
    list_display = ['question.content']
'''

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnsweredQuiz)

'''
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')

'''