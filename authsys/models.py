from sys import maxsize

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from quizes.models import Quiz

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    points = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    try_count = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'quiz',)

    def __str__(self):
        return f'{self.user} -> {self.quiz}'