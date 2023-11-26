from django.shortcuts import render, redirect
from django.views import View
from .models import MedicalTest
from .forms import MedicalTestForm, QuestionForm, ChoiceForm

class CreateMedicalTestView(View):
    def get(self, request):
        test_form = MedicalTestForm()
        question_form = QuestionForm()
        choice_form = ChoiceForm()
        return render(request, 'create_medical_test.html', {'test_form': test_form, 'question_form': question_form, 'choice_form': choice_form})

    def post(self, request):
        test_form = MedicalTestForm(request.POST)
        question_form = QuestionForm(request.POST)
        choice_form = ChoiceForm(request.POST)

        if test_form.is_valid() and question_form.is_valid() and choice_form.is_valid():
            test = test_form.save()
            question = question_form.save(commit=False)
            question.test = test
            question.save()
            choice = choice_form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('medical_test_list')

        return render(request, 'create_medical_test.html', {'test_form': test_form, 'question_form': question_form, 'choice_form': choice_form})


class MedicalTestListView(View):
    def get(self, request):
        medical_tests = MedicalTest.objects.all()
        return render(request, 'medical_test_list.html', {'medical_tests': medical_tests})

class UnansweredCustomerList(View):
    def get(self, request):
        return HttpResponse("List of unanswered customers")

class AnsweredCustomerList(View):
    def get(self, request):
        return HttpResponse("List of answered customers")

def admin_page(request):
    return HttpResponse("Hello, admin!")
