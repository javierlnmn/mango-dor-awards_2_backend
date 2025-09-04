from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Candidate
from .serializers import CandidateSerializer


class CandidateView(ReadOnlyModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
