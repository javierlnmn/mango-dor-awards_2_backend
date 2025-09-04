from rest_framework.serializers import ModelSerializer

from .models import SiteParameters


class SiteParametersSerializer(ModelSerializer):
    class Meta:
        model = SiteParameters
        fields = ('winners_reveal_date',)
