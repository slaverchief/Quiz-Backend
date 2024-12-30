from pydoc import resolve
from urllib.request import Request

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from QuizAPI.settings import DEBUG
from QuizAPI.decorators import handle_exceptions
from QuizAPI.exceptions import HandledException
from authsys.models import Result
from .serializers import *
from .models import *
from QuizAPI.permissions import *
from rest_framework.permissions import IsAuthenticated

class QuizApiView(APIView):
    permission_classes = (IsAuthenticated, )

    @handle_exceptions
    def get(self, request):
        quizes = QuizSerializer(instance = Quiz.objects.all(), many=True)
        return Response(quizes.data)

    @handle_exceptions
    def post(self, request):
        quiz = request.data.get('quiz')
        if not quiz:
            raise HandledException("Specify the quiz id")
        try:
            quiz = Quiz.objects.get(pk=int(quiz))
        except ObjectDoesNotExist:
            raise HandledException("No such a quiz")
        questions = quiz.questions.all()
        point_step = 100/len(questions)
        points = 0
        for q in questions:
            ans = request.data.get(str(q.pk))
            right_answer =  "/media/"+str(q.right_answer)
            if ans == right_answer:
                points += point_step
        user_result = None
        try:
            user_result = Result.objects.get(user=request.user, quiz=quiz)
            if not DEBUG and (user_result.try_count >= 2 or user_result.points >= 50):
                return Response(status=460)
            user_result.try_count += 1
            user_result.points = points
            user_result.save()
        except ObjectDoesNotExist:
            user_result = Result.objects.create(user=request.user, quiz=quiz, points=points)
        return Response({'res': round(user_result.points)})

class QuestionApiView(APIView):
    permission_classes = (IsAuthenticated, )

    @handle_exceptions
    def get(self, request, quiz):
        questions = QuestionSerializer(instance=Question.objects.filter(quiz=quiz), many=True)
        if not questions.data:
            raise HandledException('No questions for such a quiz')
        return Response(questions.data)


