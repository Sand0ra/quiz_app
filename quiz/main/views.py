from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .models import Game, Question
from .serializers import GameSerializer, QuestionSerializer


class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionAnswerView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'pk'

    def post(self, request, pk):
        question = Question.objects.get(pk=pk)
        selected_answer = request.data.get('selected_answer')
        if selected_answer is not None:
            try:
                selected_answer = int(selected_answer)
                correct_answer_id = question.answers.filter(is_correct=True).first().id
                if selected_answer == correct_answer_id:
                    return Response({"Ураа!!!": "Вы ответили правильно!"})
            except (ValueError, AttributeError):
                pass
        return Response({"Нет!": "Неверный ответ."})
