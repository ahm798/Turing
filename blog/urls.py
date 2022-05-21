from django.urls import path
from . import views


# urlpatterns = [
#     path('articles/', views.Article_List_View, name="articleList"),
#     path('topics/', views.Topic_List_View, name="topiclist"),
#     path('', views.Article_List_View, name="articleList"),
#     path('articles/myarticle', views.User_Article_List_View, name="myarticle"),
#     path('articles/<int:pk>/', views.Article_Detail_View, name="article"),
#     path('articles/<int:pk>/update/', views.Article_Update_View, name="update-article"),
#     path('articles/<int:pk>/destroy/', views.Article_Destroy_view, name="destroy-article"),
#     path('articles/create/', views.Article_Create_View, name="create-article"),
#     path('articles/createOrlist/', views.Article_List_Create_View, name="create-article"),
# ]


urlpatterns =[
    path('', views.articleListView, name='articles'),
    path('<str:pk>/', views.articleDetailView, name="get-article"),
    path('art/add/', views.create_article, name='create-article'),
    path('edit/<str:pk>/', views.articleUpdateView, name="edit-article"),
    path('delete/<str:pk>/', views.articleDeleteView, name="delete-article"),
    path('edit-comment/<str:pk>/', views.articleCommentUpdateView, name="edit-article-comment"),
    path('delete-comment/<str:pk>/', views.articleCommentDeleteView, name="delete-article-comment"),
    path('vote/', views.voteUpdateView, name='article-vote'),
    ]
