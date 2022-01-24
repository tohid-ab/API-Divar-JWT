from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register('home', ArticleViewSet)
router.register('center', ArticleCenterViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("test", ArticleTestView.as_view(), name='home-Test'),
    path("home/<int:pk>/", HomeDetaile.as_view(), name='home-detail'),
    path("home/<int:pk>/update", HomeDetaileUpdate.as_view(), name='home-detail-update'),
    path("home/<int:pk>/delete", HomeDetaileDelete.as_view(), name='home-detail-delete'),
    path("users/", UserleArticle.as_view(), name='user'),
    path("users/create", CreateUserleArticle.as_view(), name='create-user'),
    path("users/<int:pk>/", DetailUserArticle.as_view(), name='user-detail'),
]