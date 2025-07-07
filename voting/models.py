from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import CustomUser
from candidates.models import Candidate


class Category(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    winner = models.ForeignKey(
        Candidate,
        on_delete=models.PROTECT,
        related_name='won_categories',
        blank=True,
        null=True,
    )
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def user_category_voting_complete(self, user):
        votes_in_category = self.votes.filter(user=user).count()
        return False if votes_in_category < 3 else True

    def __str__(self):
        return f'{self.name} ({self.code})'


class Vote(models.Model):
    VOTING_POINTS_CHOICES = [
        (1, '1 point'),
        (2, '2 points'),
        (4, '4 points'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='votes')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='votes')
    points = models.IntegerField(choices=VOTING_POINTS_CHOICES)

    class Meta:
        unique_together = ['user', 'candidate', 'category']

    def clean(self):
        votes_qs = Vote.objects.filter(user=self.user, category=self.category)
        if self.pk:
            votes_qs = votes_qs.exclude(pk=self.pk)

        errors = {}

        if votes_qs.filter(candidate=self.candidate).exists():
            errors['candidate'] = 'You have already voted for this candidate in this category.'

        if votes_qs.filter(points=self.points).exists():
            errors['points'] = f'Already assigned {self.get_points_display()} points in this category.'

        if votes_qs.count() >= 3:
            errors['__all__'] = 'You have already voted 3 times in this category.'

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f'{self.user} voted {self.get_points_display()} points for {self.candidate} in {self.category}'
