from django import forms
from django.db.models import fields
from .models import Exam, Option, Question

class CreateExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('title', 'status', 'num_questions', 'subject', 'passing_marks')

        labels = {
            'title': '',
            'status': '',
            'num_questions': '',
            'subject': '',
            'passing_marks': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
            'status': forms.Select(attrs={'class': 'form-select','placeholder':'Status'}),
            'num_questions': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'No. of questions'}),
            'subject': forms.Select(attrs={'class': 'form-select','placeholder':'Subject'}),
            'passing_marks': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Passing Marks'}),
        }

class CreateQuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ()
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
            'status': forms.Select(attrs={'class': 'form-select','placeholder':'Status'}),
            'num_questions': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'No. of questions'}),
            'subject': forms.Select(attrs={'class': 'form-select','placeholder':'Subject'}),
            'passing_marks': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Passing Marks'}),
        }

CreateQuestionsFormSet = forms.inlineformset_factory(
                            Question,
                            Option, 
                            extra=4, 
                            form=CreateQuestionsForm
                        )