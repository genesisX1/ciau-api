from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BlogPostViewSet, PortfolioProjectViewSet, MediaFileViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'blog', BlogPostViewSet)


router.register(
    'medias', MediaFileViewSet
)

router.register(
    'portfolio', PortfolioProjectViewSet
)

urlpatterns = router.urls

