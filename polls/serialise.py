from rest_framework import serializers
from polls.models import Question,Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes']

class CommentSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source="question",read_only=True)
    
    class Meta:
        model = Choice
        fields = ['question_text','choice_text','votes','question_id']
