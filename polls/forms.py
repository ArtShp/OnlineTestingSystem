from django import forms
from polls.models import Answer


class _Form(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    price = forms.DecimalField(min_value=0, max_value=10, max_digits=3)
    author_email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)


class AnswerForm(forms.ModelForm):
    class Meta:
        ans = Answer
        fields = ('content', 'TBD')