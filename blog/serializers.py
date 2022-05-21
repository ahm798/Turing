from rest_framework import serializers
from .models import Article, Topic
from account.serializers import  UserInlineSerializer

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name']


class ArticleSerializerDetial(serializers.ModelSerializer):
    topic = TopicSerializer()
    owner = UserInlineSerializer(read_only=True)
    class Meta():
        model = Article
        fields = ['id','topic','owner','title', 'slug' ,'content','publish', 'created', 'updated', 'status']
