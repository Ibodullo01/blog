from rest_framework import serializers

from app.models import Category, Blog, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'


class BlogsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'description', 'category']


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'description']

class BlogDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = []

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['pk', 'text']
