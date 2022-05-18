from rest_framework import generics, permissions, authentication
from .permissions import IsMember, IsOwner
from .serializers import ArticleSerializerDetial
from .models import Article


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerDetial
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsMember]

Article_Detail_View = ArticleDetailView.as_view()


#____________________________ListAPIView____________________________________________#
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerDetial
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsMember]


Article_List_View = ArticleListView.as_view()
#____________________________user ListAPIView____________________________________________#
class UserArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerDetial
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsMember]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        request = self.request
        user = request.user
        return qs.filter(owner=request.user)

User_Article_List_View = UserArticleListView.as_view()


#____________________________CreateApiView____________________________________________#

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerDetial
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsMember]


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

Article_Create_View = ArticleCreateView.as_view()


#____________________________ListCreateView____________________________________________#

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerDetial
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [IsMember]

Article_List_Create_View = ArticleListCreateView.as_view()

#____________________________ListCreateView____________________________________________#

class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerDetial

    permission_classes = [permissions.IsAdminUser, IsOwner]
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

    def perform_update(self, serializer):
        instance = serializer.save()


Article_Update_View = ArticleUpdateView.as_view()


#____________________________ListCreateView____________________________________________#

class ArticleDestroyView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializerDetial

    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsOwner]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

Article_Destroy_view = ArticleDestroyView.as_view()


