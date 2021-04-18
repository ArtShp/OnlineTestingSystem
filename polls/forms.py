from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, NullBooleanSelect
from polls.models import Answer, Question, Quiz

'''
class QuizForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    price = forms.DecimalField(min_value=0, max_value=10, max_digits=3)
    author_email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    #questions = Question.objects.filter(quiz_id=quiz_id)
    questions = Question.objects.all()
'''

class QuizForm(ModelForm):
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
