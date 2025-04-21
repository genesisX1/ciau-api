from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import BlogPost, PortfolioProject, MediaFile
from .serializers import BlogPostSerializer, PortfolioProjectSerializer, MediaFileSerializer

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff  # Seuls les admins sont autorisés

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]  # Autoriser tout le monde
    # permission_classes = [permissions.IsAuthenticated]  # Accès restreint aux admins

class PortfolioProjectViewSet(viewsets.ModelViewSet):
    queryset = PortfolioProject.objects.all().order_by('-created_at')
    serializer_class = PortfolioProjectSerializer
    permission_classes = [permissions.AllowAny]  # Autoriser tout le monde
    # permission_classes = [permissions.IsAuthenticated]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    # permission_classes = [IsAdminUser]  # Seuls les admins peuvent gérer les médias
    permission_classes = [permissions.AllowAny]
