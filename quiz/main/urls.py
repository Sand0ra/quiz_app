from django.urls import path
from . import views


urlpatterns = [
    path('games/', views.GameList.as_view(), name='game-list'),
    path('game/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionAnswerView.as_view(), name='question-detail'),
]
