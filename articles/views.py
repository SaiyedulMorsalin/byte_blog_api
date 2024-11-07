from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.


class ArticleAPIView(APIView):
    def get(self,request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article,many=True)
        return Response(serializer.data)
        