from rest_framework import serializers
from .models import *


class BoardListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Board
        fields = ("name", "description")


class TopicsListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Topic
        fields = '__all__'


class BoardDetailSerializer(serializers.ModelSerializer):
    topics = TopicsListSerializer(many=True)

    class Meta:

        model = Board
        exclude = ("is_active", )

    # @staticmethod
    # def get_posts(obj):
    #     return BoardDetailSerializer(Board.objects.all().prefetch_related('topic_set'), many=True).data


class TopicCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Topic
        fields = "__all__"
