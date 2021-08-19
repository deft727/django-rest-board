from django.urls import path

from .views import *

urlpatterns = [
                path("boards/", BoardsListView.as_view()),
                path("boards/<int:pk>/", BoardDetailView.as_view()),
                path("topics/", TopicsCreateView.as_view())
]