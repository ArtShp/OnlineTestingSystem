from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.show_all_quiz, name='show_all_quiz'),
    path('<int:quiz_id>/', views.show_quiz, name='show_quiz'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('<int:quiz_id>/start_quiz/', views.start_quiz, name='start_quiz'),
    path('<int:quiz_id>/answers', views.show_answered_quiz, name='show_answered_quiz')
]
