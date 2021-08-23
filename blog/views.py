import board as board
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


# class BoardsListView(APIView):
#
#     def get(self, request):
#
#         boards = Board.objects.all()
#         serializer = BoardListSerializer(boards, many=True)
#         return Response(serializer.data)


class BoardsListView(APIView):

    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

# class BoardDetailView(APIView):
#
#     def get(self, request, pk):
#         boards = Board.objects.get(id=pk)
#         serializer = BoardDetailSerializer(boards)
#
#         return Response(serializer.data)


class BoardDetailView(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer


class TopicsCreateView(APIView):

    def post(self, request):
        topics = TopicCreateSerializer(data=request.data)
        print(topics)
        if topics.is_valid():
            # topics.board = 1
            # topics.starter = 1
            topics.save()
        return Response(status=201)

"""
{
   "subject":"fromPOSTtest",
    "board":1,
    "starter":1
}
"""

class TopicsDetailView(APIView):

    def get(self, request, **kwargs):
        topic = Topic.objects.get(id=kwargs.get("topic_pk"))
        # posts = topic.posts.all()
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data)
