from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.models import Category, Comments, Blog
from app.api.v1.serializerss import  CategorySerializer, CommentsSerializer, BlogsSerializer, BlogUpdateSerializer, BlogsCreateSerializer
from app.permisions import IsOwner


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]


@api_view(http_method_names=['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog_create(request):
    serializer = BlogsCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


def blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST', 'PUT', 'DELETE'])
def blogs_detail(request, pk):
    if request.method == 'PUT':
        blogs = get_object_or_404(Blog, pk=pk)
        serializer = BlogUpdateSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        blogs = get_object_or_404(Blog, pk=pk)
        blogs.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['POST', 'GET'])
def comments(request):
    if request.method == 'GET':
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST', 'DELETE'])
def comments_detail(request, pk):
    if request.method == 'POST':
        comments = get_object_or_404(Comments, pk=pk)
        serializer = CommentsSerializer(comments)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        comments = get_object_or_404(Comments, pk=pk)
        comments.delete(pk)
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer


class BlogUpdateAPIView(APIView):
    permission_classes = [IsOwner]


    def put(self , request , pk):
        blog = get_object_or_404(Blog , pk=pk)
        self.check_object_permissions(self.request , blog)
        serializer = BlogUpdateSerializer(blog , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        return Response(serializer.errors , status = 400)

class BlogDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Blog.objects.all()


