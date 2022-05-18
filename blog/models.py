from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q

class ModelQuerySet(models.QuerySet):
    def is_published(self):
        return self.filter(status='published')

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.filter(lookup)
        if user is not None:
            qs = qs.filter(owner__username=user)
        return qs

class ArticleManger(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ModelQuerySet(self.model, using=self.db)

    def search(self, query, user=None):
        return self.get_queryset().is_published().search(query=query, user=user)


class Topic(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))

    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = ArticleManger()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title