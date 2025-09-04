from rest_framework import serializers

from .models import Category, Vote


class CategorySerializer(serializers.ModelSerializer):
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
