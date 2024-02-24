from rest_framework import serializers
from .models import Question,  UserResponse

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['pk', 'user_response', 'pub_date']


class QuestionSerializer(serializers.ModelSerializer):
    userresponse_set = UserResponseSerializer(many=True, read_only=True)
    responses = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['pk', 'question_text', 'pub_date', 'upvotes', 'expert_response', 'userresponse_set', 'ai_response', 'responses']

    def get_responses(self, obj):
        return []