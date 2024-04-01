from django.urls import path
from rest_framework.routers import DefaultRouter

from app.api.v1.view import CategoryCreateAPIView, blogs_detail, comments, blog_create, BlogViewSet

router = DefaultRouter()

router.register('blogs' , BlogViewSet)

urlpatterns = [
    path('category/', CategoryCreateAPIView.as_view(), name='category'),
    path('blogs/', blog_create, name='blogs'),
    path('blogs/<int:pk>', blogs_detail, name='blogs_detail'),
    path('comments/', comments, name='comments'),
    path('comments/<int:pk>', comments, name='comments_detail')
]

urlpatterns += router.urls