from django.contrib.auth import get_user_model
from .permission import IsAutherOrReadOnly, IsSuperUserOrStaffReadOnly, IsStaffOrReadOnly
from .serializers import UserSerializers, BlogSerializers
from rest_framework.viewsets import ModelViewSet
from blog.models import Blog


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    filterset_fields = ['is_active', 'auther']
    search_fields = ['title', 'auther__username', 'text']
    ordering_fields = ['create_time']

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAutherOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly,)
