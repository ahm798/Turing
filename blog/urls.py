from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.Article_List_View, name="articleList"),
    path('topics/', views.Topic_List_View, name="topiclist"),
    path('', views.Article_List_View, name="articleList"),
    path('articles/myarticle', views.User_Article_List_View, name="myarticle"),
    path('articles/<int:pk>/', views.Article_Detail_View, name="article"),
    path('articles/<int:pk>/update/', views.Article_Update_View, name="update-article"),
    path('articles/<int:pk>/destroy/', views.Article_Destroy_view, name="destroy-article"),
    path('articles/create/', views.Article_Create_View, name="create-article"),
    path('articles/createOrlist/', views.Article_List_Create_View, name="create-article"),
]