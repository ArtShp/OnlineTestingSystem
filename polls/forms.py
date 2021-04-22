from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, NullBooleanSelect
from django import forms
from polls.models import Answer, Question, Quiz, AnsweredQuiz

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

class QuizForm(ModelForm):
    class Meta:
        model = AnsweredQuiz
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Name'
            })
        }

