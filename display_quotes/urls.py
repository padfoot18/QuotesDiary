from django.urls import path
from display_quotes import views


urlpatterns = [
    path("search/", views.search_results, name="search_results"),
    path("search_form/", views.SearchResultsView.as_view()),
    path("<str:category>/", views.QuotesList.as_view(), name="view"),
]
