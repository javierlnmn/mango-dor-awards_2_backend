from rest_framework import serializers

from candidates.serializers import CandidateLiteSerializer, CandidateSerializer

from .models import Category, Vote


class CategorySerializer(serializers.ModelSerializer):
    winner = CandidateSerializer(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class VotingSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if Vote.objects.filter(
            category=attrs['category'], user=attrs['user'], points=attrs['points']
        ).exists():
            raise serializers.ValidationError('You have already voted for this category with this points')
        if Vote.objects.filter(
            category=attrs['category'], user=attrs['user'], candidate=attrs['candidate']
        ).exists():
            raise serializers.ValidationError('You have already voted 3 times in this category')
        if Vote.objects.filter(category=attrs['category'], user=attrs['user']).count() >= 3:
            raise serializers.ValidationError('You have already voted 3 times in this category')
        if attrs['points'] not in [choice[0] for choice in Vote.VOTING_POINTS_CHOICES]:
            raise serializers.ValidationError('Invalid voting point')
        return attrs

    class Meta:
        model = Vote
        fields = '__all__'


class CandidateVotesSummarySerializer(serializers.Serializer):
    candidate = CandidateLiteSerializer(read_only=True)
    total_votes = serializers.IntegerField(read_only=True)
    total_points = serializers.IntegerField(read_only=True)

    class Meta:
        order_by = ['-total_points', '-total_votes']


class CategoryVotingRankingSerializer(serializers.Serializer):
    category = CategorySerializer(read_only=True)
    candidates = CandidateVotesSummarySerializer(many=True, read_only=True)
