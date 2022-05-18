from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/blog/', include('blog.urls')),
    path('api/account/', include('account.urls')),
    path('api/auth/', obtain_auth_token),
]