from django.db import models

class MedicalTest(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField('Question', related_name='medical_tests')

class Question(models.Model):
    text = models.CharField(max_length=255)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
