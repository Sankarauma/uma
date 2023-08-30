from django.shortcuts import render
from .models import Question

def quiz_list(request):
    questions = Question.objects.all()
    return render(request, 'quiz_app/quiz_list.html', {'questions': questions})
