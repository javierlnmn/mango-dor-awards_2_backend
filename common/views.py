from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SiteParameters
from .serializers import SiteParametersSerializer


class SiteParametersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        config = SiteParameters.load()
        serializer = SiteParametersSerializer(config)
        return Response(serializer.data)
