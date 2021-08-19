from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class BoardsListView(APIView):

    def get(self,request):

        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)


class BoardDetailView(APIView):

    def get(self, request, pk):
        boards = Board.objects.get(id=pk)
        serializer = BoardDetailSerializer(boards)

        return Response(serializer.data)


class TopicsCreateView(APIView):
    def post(self, request):
        topics = TopicCreateSerializer(data=request.data)
        print(topics)
        if topics.is_valid():
            topics.save()
        return Response(status=201)

"""
{
   'subject':'fromPOST',
    'board':1,
}
"""


# starter