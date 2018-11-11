from django.urls import path
from display_quotes import views


urlpatterns = [
    path('', views.check, name='check'),
    path('<str:category>/', views.QuotesList.as_view()),
]
