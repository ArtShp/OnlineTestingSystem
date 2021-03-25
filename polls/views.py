from django.shortcuts import get_object_or_404, render

from .models import Question, Quiz

def show_all_quiz(request):
    quizzes = Quiz.objects.order_by('-pub_date')
    return render(request, 'polls/show_all_quiz.html', {'quizzes': quizzes})
def show_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'polls/show_quiz.html', {'quiz': quiz, 'quiz_id': quiz_id})
