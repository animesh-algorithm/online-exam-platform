from django.db import models
from django.urls import reverse

EXAM_STATUS_CHOICE = [
    ('offline', 'offline'),
    ('online', 'online')
]

class Subject(models.Model):
    subject_code = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Exam(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=EXAM_STATUS_CHOICE, default='offline')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
    num_questions = models.IntegerField()
    passing_marks = models.FloatField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('create_questions', args=[str(self.id)])

    def get_questions(self):
        return self.question_set.all()

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam')
    question = models.CharField(max_length=255, default='demo question')
    answer = models.CharField(max_length=255)
    marks = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.exam) + " | " + self.question
    
    def get_absolute_url(self):
        return reverse('create_questions', kwargs={
                'pk':self.exam.id
            })
    
    # def get_answers(self):
    #     return self.answer_set.all()

# class Answer(models.Model):
#     text = models.CharField(max_length=255)
#     correct = models.BooleanField(default=False)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=True)

#     def __str__(self):
#         return str(self.question) + " | " + self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')
    option = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question) + ' | '+  self.option
    
    def get_absolute_url(self):
        return reverse('create_options', kwargs={
            'pk':self.question.exam.id,
            'question_id':self.question.id
        })