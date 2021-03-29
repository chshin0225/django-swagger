from django.urls import path
from . import views

urlpatterns = [
    path('secondhello/', views.SecondHelloView.as_view()),
]