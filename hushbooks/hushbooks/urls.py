from django.contrib import admin
from django.urls import path, include, re_path
from book.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/booklist/', BookAPIView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
