from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, NullBooleanSelect
from django import forms
from polls.models import Answer, Question, Quiz

'''
class QuizForm(ModelForm):
    class Meta:
        model = 
'''
    #name = forms.CharField(max_length=25, required=True)

    #questions = Question.objects.filter(quiz_id=quiz_id)
    #questions = Question.objects.all()


class CreateQuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'random_order', 'pub_date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Quiz name'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Description'
            }),
            'random_order': NullBooleanSelect(attrs={
                'placeholder': 'Random order'
            }),
            'pub_date': DateTimeInput(attrs={
                'placeholder': 'Published date'
            })
        }
