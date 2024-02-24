from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.ai import generate_question_answer
import threading


class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    ai_response = models.CharField(max_length=2000, blank=True)
    expert_response = models.CharField(max_length=2000, blank=True)

    # foreign keys on me:
    # expertresponse_set: ExpertResponse object
    # userresponse_set: UserResponse object
    def generate_question_answer(self):
        try:
            self.ai_response = generate_question_answer(self.question_text)
            self.save()
        except Exception as e:
            # Log the exception
            print(f"Error generating answer: {e}")
    @staticmethod
    def create_question(question_text):
        question = Question.objects.create(question_text=question_text)
        # generate_question_answer in a separate thread
        t = threading.Thread(target=question.generate_question_answer)
        t.start()
        return question



class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_response = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
