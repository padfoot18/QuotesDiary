from django.urls import path
from display_quotes import views


urlpatterns = [
    path('', views.check, name='check'),
    path('search/', views.search_results, name='search_results'),
    path('<str:category>/', views.QuotesList.as_view()),
]
