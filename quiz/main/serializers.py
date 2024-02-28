from rest_framework import serializers
from .models import Game, Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(read_only=True)
    selected_answer = serializers.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], write_only=True, )

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers', 'selected_answer']
        read_only_fields = ['answers']

    def get_answers(self, obj):
        return [{'id': answer.id, 'text': answer.text} for answer in obj.answers.all()]


class GameQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text']


class GameSerializer(serializers.ModelSerializer):
    questions_1 = serializers.SerializerMethodField()
    questions_2 = serializers.SerializerMethodField()
    questions_3 = serializers.SerializerMethodField()
    questions_4 = serializers.SerializerMethodField()
    questions_5 = serializers.SerializerMethodField()
    questions_6 = serializers.SerializerMethodField()
    questions_7 = serializers.SerializerMethodField()
    questions_8 = serializers.SerializerMethodField()
    questions_9 = serializers.SerializerMethodField()
    questions_10 = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'title', 'questions_1', 'questions_2', 'questions_3', 'questions_4', 'questions_5',
                  'questions_6', 'questions_7', 'questions_8', 'questions_9', 'questions_10']

    def get_questions_1(self, obj):
        return self.get_question_text(obj, 0)

    def get_questions_2(self, obj):
        return self.get_question_text(obj, 1)

    def get_questions_3(self, obj):
        return self.get_question_text(obj, 2)

    def get_questions_4(self, obj):
        return self.get_question_text(obj, 3)

    def get_questions_5(self, obj):
        return self.get_question_text(obj, 4)

    def get_questions_6(self, obj):
        return self.get_question_text(obj, 5)

    def get_questions_7(self, obj):
        return self.get_question_text(obj, 6)

    def get_questions_8(self, obj):
        return self.get_question_text(obj, 7)

    def get_questions_9(self, obj):
        return self.get_question_text(obj, 8)

    def get_questions_10(self, obj):
        return self.get_question_text(obj, 9)

    def get_question_text(self, obj, index):
        questions = obj.questions.all()
        if len(questions) > index:
            return questions[index].text
        return None
