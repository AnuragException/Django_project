from polls.models import Question, Choice
from rest_framework.views import APIView
from polls.serialise import CommentSerializer
from rest_framework.response import Response

class join_api(APIView):

    def get(self, request, pk=None, format=None):
        
        question_id_filter = self.request.query_params.get('question_id_filter', None)
        if question_id_filter: # check if key is not Nonel
            queryset = Choice.objects.filter(question_id=question_id_filter)
            serializer = CommentSerializer(queryset,many = True)
            return Response(serializer.data)

        queryset = Choice.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

