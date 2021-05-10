from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ExamView.as_view(), name='exam'),
    path('create/', CreateExamView.as_view(), name='create_exam'),
    path('<int:pk>/questions/create', CreateQuestionsView.as_view(), name='create_questions'),
    # path('<int:pk>/questions/<int:question_id>/options/', CreateOptionsView.as_view(), name='create_options'),
]

# Also include static files here...