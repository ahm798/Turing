from django.urls import path, include

urlpatterns = [
    path('api/blog/', include('blog.urls')),
    path('blog/account/', include('account.urls')),
]