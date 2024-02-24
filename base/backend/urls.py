from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('hello/', views.HelloWorldView.as_view(), name='hello'),
    path('questions/', views.QuestionListView.as_view(), name='questions'),
    path('create_question/', views.CreateQuestionView.as_view(), name='create_question'),
    path('upvote/', views.QuestionUpvoteView.as_view(), name='upvote'),
    path('expert_response/', views.QuestionResponseExpertView.as_view(), name='expert_response'),
    path('user_response/', views.QuestionResponseUserView.as_view(), name='user_response'),

]