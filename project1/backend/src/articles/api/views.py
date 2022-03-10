from rest_framework.generics import ListAPIView, RetriveAPIView

from articles.models import Article
from .serialiazers import ArticleSerializers

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetailView(RetriveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
