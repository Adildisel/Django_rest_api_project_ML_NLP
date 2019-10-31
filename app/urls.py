from django.urls import path

from .views import *

urlpatterns = [
    path('comments/', ParserAPIView.as_view()),
    path('urls_video_youtube/', VideoIdAPIView.as_view()),
]
