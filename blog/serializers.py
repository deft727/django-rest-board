from pyexpat import model

from rest_framework import serializers
from .models import *


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class BoardListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Board
        fields = ("id", "name", "description")


class TopicsListSerializer(serializers.ModelSerializer):
    # posts = RecursiveSerializer(many=True)
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


class BoardCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ("name", "description")


class TopicCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Topic
        fields = "__all__"


class PostsListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = "__all__"


class TopicDetailSerializer(serializers.ModelSerializer):

    posts = PostsListSerializer(many=True)

    class Meta:

        model = Topic
        fields = "__all__"
