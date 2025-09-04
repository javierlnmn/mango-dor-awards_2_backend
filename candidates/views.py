from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(ReadOnlyModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [AllowAny]
