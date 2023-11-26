from django import forms
from .models import MedicalTest, Question, Choice

class MedicalTestForm(forms.ModelForm):
    class Meta:
        model = MedicalTest
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']
