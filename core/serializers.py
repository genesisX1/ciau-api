from html import unescape
from rest_framework import serializers
from .models import BlogPost, PortfolioProject, MediaFile, CustomUser

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'title', 'file']

class PortfolioProjectSerializer(serializers.ModelSerializer):
    media_files = MediaFileSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()

    
    def get_description(self, obj):
        return unescape(obj.description)
    class Meta:
        model = PortfolioProject
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_admin']

