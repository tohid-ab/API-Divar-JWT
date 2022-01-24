from django.urls import path
from .views import *

app_name = 'divar'

urlpatterns = [
    path("", FierstView.as_view(), name='home'),
    path("<int:pk>/", ArticleDetail.as_view(), name='detail'),
]