from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.show_all_quiz, name='show_all_quiz'),
    path('<int:quiz_id>/', views.show_quiz, name='show_quiz'),
]
