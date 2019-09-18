from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register('snippets', SnippetViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
