from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import AppUser, Question, Comment
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AppUserForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib import messages


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
        form = QuestionForm(request.POST, request.FILES)
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
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'guide_app/question_form.html', {'form': form})

@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.user != request.user:
        messages.error(request, "You do not have permission to delete this question.")
        return redirect('question_detail', pk=pk)
    if request.method == 'POST':
        question.delete()
        messages.success(request, "Question deleted successfully.")
        return redirect('questions')
    return render(request, 'guide_app/question_confirm_delete.html', {'object': question})



def question_list(request):
    questions = Question.objects.all()
    return render(request, 'guide_app/question_list.html', {'questions': questions})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'guide_app/question_detail.html', {'question': question})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.author = request.user 
            comment.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = CommentForm()
    return render(request, 'guide_app/question_detail.html', {'question': question, 'form': form})

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('questions')  # Redirect to the question list after deletion
    template_name = 'guide_app/question_confirm_delete.html'  # Confirmation template

    def get_queryset(self):
        """ Ensure only the question owner can delete the question. """
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)
    

# User registration
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'guide_app/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'guide_app/login.html'

    def get(self, request, *args, **kwargs):
        messages.info(request, "Please log in to continue.")
        return super().get(request, *args, **kwargs)
