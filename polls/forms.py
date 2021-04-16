from django import forms
from polls.models import Answer, Question, Quiz


class QuizForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    price = forms.DecimalField(min_value=0, max_value=10, max_digits=3)
    author_email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    #questions = Question.objects.filter(quiz_id=quiz_id)
    questions = Question.objects.all()




class QuestionForm(forms.ModelForm):
    '''
    class Meta:
        ans = Answer
        fields = ('content', 'TBD')
    '''