from django.urls import path
from manage_quotes import views


urlpatterns = [
    path('add/', views.AddQuote.as_view(), name='add'),
    path('delete/<int:pk>/', views.DeleteQuote.as_view(), name='delete'),
    path('edit/<int:pk>/', views.EditQuote.as_view(), name='edit'),
]
