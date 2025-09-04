from rest_framework import serializers

from .models import Candidate, CandidateImage, Gender, Nationality


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class CandidateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateImage
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    images = CandidateImageSerializer(many=True, read_only=True)
    gender = GenderSerializer(read_only=True)
    nationalities = NationalitySerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = '__all__'
