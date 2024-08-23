from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    SlugRelatedField,
)

from posts.models import Comment, Group, Post


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'pub_date',
            'author',
            'image',
            'group',
        )


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    post = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created',
        )


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )
