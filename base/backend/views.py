from django.shortcuts import render
 

from .models import Question
from .serializers import QuestionSerializer

from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World"})

# QuestionViewSet

# upvote question
class QuestionUpvoteView(APIView):
    def post(self, request):
        pk = request.data.get('question')
        question = get_object_or_404(Question, pk=pk)
        question.upvotes += 1
        question.save()
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

# respond to question 

class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all().order_by('-upvotes', 'pk')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class CreateQuestionView(APIView):
    def post(self, request):
        question_text = request.data.get('question_text')
        # raise an error if question_text is empty
        if not question_text:
            return Response({"question_text": "This field may not be blank."}, status=400)
        question = Question.create_question(question_text)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

class QuestionResponseExpertView(APIView):
    def post(self, request):
        pk = request.data.get('question')
        question = get_object_or_404(Question, pk=pk)
        expert_response = request.data.get('expert_response')
        # raise an error if expert_response is empty
        if not expert_response:
            return Response({"expert_response": "This field may not be blank."}, status=400)
        question.expert_response = expert_response
        question.save()
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

class QuestionResponseUserView(APIView):
    def post(self, request):
        pk = request.data.get('question')
        question = get_object_or_404(Question, pk=pk)
        user_response = request.data.get('user_response')
        # raise an error if user_response is empty
        if not user_response:
            return Response({"user_response": "This field may not be blank."}, status=400)
        question.userresponse_set.create(user_response=user_response)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

