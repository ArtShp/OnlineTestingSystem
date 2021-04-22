from django.shortcuts import get_object_or_404, render, redirect
from .models import Quiz, Question, Answer
from .forms import CreateQuizForm, QuizForm

def show_all_quiz(request):
    quizzes = Quiz.objects.order_by('-pub_date')
    return render(request, 'polls/show_all_quiz.html', {'quizzes': quizzes})

def show_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz_id)
    answers = Answer.objects.all()
    return render(request, 'polls/show_quiz.html', {'quiz': quiz,
                                                    'quiz_id': quiz_id,
                                                    'questions': questions,
                                                    'answers': answers})

def create_quiz(request):
    error = ''
    if request.method == 'POST':
        form = CreateQuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Form error'

    form = CreateQuizForm()

    return render(request, 'polls/create_quiz.html', {'form': form,
                                                      'error': error})

def start_quiz(request, quiz_id):
    error = ''
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Form error'

    form = QuizForm()

    return render(request, 'polls/start_quiz.html', {'quiz_id': quiz_id,
                                                     'form': form,
                                                     'error': error})
