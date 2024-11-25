from django.urls import path, include
from .views import *

urlpatterns = [
    path('quiz', QuizApiView.as_view()),
    path('question/<int:quiz>', QuestionApiView.as_view()),
]
