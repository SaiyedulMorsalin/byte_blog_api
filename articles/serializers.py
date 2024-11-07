from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    cover_image_url = serializers.SerializerMethodField("get_cover_image_url")
    class Meta:
        model = Article
        # fields = ['title']
        fields = '__all__' 
        include =('cover_image_url',)
       
        

    def get_cover_image_url(self,obj):
        if obj:
            return f"http://127.0.0.1:8000{obj.cover_image.url}"
        return None