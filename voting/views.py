from django.db import models
from django.db.models import Count, Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from candidates.models import Candidate

from .models import Category
from .serializers import CategorySerializer, CategoryVotingRankingSerializer, VotingSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'], url_path='category-votes')
    def category_votes(self, request, pk=None, *args, **kwargs):
        category = self.get_object()

        candidates_with_votes = Candidate.objects.filter(votes__category=category).annotate(
            total_votes=Count('votes', filter=models.Q(votes__category=category)),
            total_points=Sum('votes__points', filter=models.Q(votes__category=category)),
        )

        serializer_data = {
            'category': category,
            'candidates': [
                {
                    'candidate': candidate,
                    'total_votes': candidate.total_votes or 0,
                    'total_points': candidate.total_points or 0,
                }
                for candidate in candidates_with_votes
            ],
        }

        serializer = CategoryVotingRankingSerializer(serializer_data)
        return Response(serializer.data)


class VotingViewSet(viewsets.ViewSet):
    serializer_class = VotingSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()
        data['user'] = user.id

        serializer = VotingSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
