from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Question(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def str(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'




# signals

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


@receiver(pre_save, sender=Question)
def limit_questions(sender, instance, **kwargs):
    if instance.game.questions.count() >= 10:
        raise ValidationError('Игра не может содержать более 10 вопросов.')


@receiver(pre_save, sender=Answer)
def limit_answers(sender, instance, **kwargs):
    if instance.question.answers.count() >= 4:
        raise ValidationError('Вопрос не может содержать более 4 ответов.')
