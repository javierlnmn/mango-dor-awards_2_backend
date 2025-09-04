from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'candidates', views.CandidateView, basename='candidate')

urlpatterns = [
    path('', include(router.urls)),
]
