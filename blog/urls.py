from django.urls import path

from .views import *

urlpatterns = [
                path("boards/", BoardsListView.as_view()),
                path("boards/<int:pk>/", BoardDetailView.as_view()),
                path("new_topic/", TopicsCreateView.as_view()),
                path("boards/<int:pk>/topic/<int:topic_pk>/", TopicsDetailView.as_view()),
]