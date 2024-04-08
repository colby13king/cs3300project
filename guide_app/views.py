from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AppUser, Question
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AppUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
# Render the HTML template index.html with the data in the context variable.
   return HttpResponse('home page')


def index(request):
   #Return index.html
   return render( request, 'guide_app/index.html')

def appuser_create_view(request):
    if request.method == 'POST':
        form = AppUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appuser_list')  # Redirect to a list view or some success page
    else:
        form = AppUserForm()
    return render(request, 'appuser_form.html', {'form': form})


@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions')
    else:
        form = QuestionForm()
    return render(request, 'guide_app/question_form.html', {'form': form})

@login_required
def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk, user=request.user)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'guide_app/question_form.html', {'form': form})

@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk, user=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('questions')
    return render(request, 'guide_app/question_confirm_delete.html', {'object': question})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'guide_app/question_list.html', {'questions': questions})