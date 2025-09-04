from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'voting', views.VotingViewSet, basename='voting')

urlpatterns = [
    path('', include(router.urls)),
]
