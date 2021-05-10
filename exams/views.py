from django.db import transaction
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Exam, Question, Option
from .forms import CreateExamForm, CreateQuestionsFormSet
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
class HomeView(ListView):
    model = Exam
    template_name = 'home.html'

class ExamView(DetailView):
    model = Exam
    template_name = 'exam_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ExamView, self).get_context_data(*args, **kwargs)
        questions = Question.objects.filter(exam=self.kwargs['pk'])
        options = Option.objects.all()
        context["questions"] = questions
        context["options"] = options
        return context

class CreateExamView(CreateView):
    model = Exam
    form_class = CreateExamForm
    template_name = 'create_exam.html'

class CreateQuestionsView(CreateView):
    model = Question
    fields = '__all__'
    template_name = 'create_questions.html'

    def get_context_data(self, **kwargs):
        data = super(CreateQuestionsView, self).get_context_data(**kwargs)
        data['exam'] = Exam.objects.get(id=self.kwargs['pk'])
        if self.request.POST:
            data['question'] = CreateQuestionsFormSet(self.request.POST)
        else:
            data['question'] = CreateQuestionsFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        question = context['question']
        with transaction.atomic():
            self.object = form.save()

            if question.is_valid():
                question.instance = self.object
                question.save()
        return super(CreateQuestionsView, self).form_valid(form)