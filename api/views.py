from .serializers import *
from rest_framework.generics import *
from rest_framework.permissions import *
from .permission import *
from rest_framework.viewsets import *
from divar.models import *
from django.contrib.auth import get_user_model
# Create your views here.
# فیلد های املاک


# class ArticleHome(ListAPIView):
#     queryset = Home.objects.all()
#     serializer_class = ArticleSerializers
#     permission_classes = (IsAdminUser,)
#
#
# class CreateArticleHome(CreateAPIView):
#     queryset = Home.objects.all()
#     serializer_class = ArticleSerializers
#     permission_classes = (IsAdminUser,)


class ArticleViewSet(ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = ArticleSerializers
    filterset_fields = ['author', 'advertising']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


class HomeDetaile(RetrieveAPIView):
    queryset = Home.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (IsAdminUser,)


class HomeDetaileUpdate(RetrieveUpdateAPIView):
    queryset = Home.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (IsUser,)


class HomeDetaileDelete(RetrieveDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (IsSuperUser,)


## فیلد های املاک


class UserleArticle(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUser,)


class CreateUserleArticle(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUser,)


class DetailUserArticle(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        self.request.auth.delete()
        return get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUser,)


#تست


class ArticleTestView(CreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializers
    permission_classes = (IsAdminUser,)


# لیست شهرها


class ArticleCenterViewSet(ModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CenterSerializers

    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]