from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Article,Topic


@register(Article)
class ArticleIndex(AlgoliaIndex):
    fields=[
        'title',
        'content',
        'owner',
        'status'
    ]
    tags = 'topic_tags'

    settings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['status'],
    }


@register(Topic)
class ArticleIndex(AlgoliaIndex):
    fields=['name']