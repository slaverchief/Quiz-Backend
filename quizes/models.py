from django.db import models



class Quiz(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    content = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    right_answer = models.FileField(upload_to="videos", null=True)
    wrong_answer1 = models.FileField(upload_to="videos", null=True)
    wrong_answer2 = models.FileField(upload_to="videos", null=True)
    wrong_answer3 = models.FileField(upload_to="videos", null=True)

    def __str__(self):
        return self.content



