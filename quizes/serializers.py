from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = ['quiz']