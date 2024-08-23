from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(ModelViewSet):
    """
    ViewSet для обработки операций, связанных с постами.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Создание нового поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """
    ViewSet для обработки операций, связанных с комментариями.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_post(self):
        """Получение поста по id из URL."""
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Получение комментариев для конкретного поста."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создание нового комментария."""
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(ReadOnlyModelViewSet):
    """
    ViewSet для обработки операций чтения, связанных с группами.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
