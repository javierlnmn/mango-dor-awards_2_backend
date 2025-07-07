from django.core.cache import cache
from django.db import models
from django.utils import timezone


class AbstractSingleton(models.Model):
    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(AbstractSingleton, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SiteParameters(AbstractSingleton):
    winners_reveal_date = models.DateField(null=True, blank=True)

    @property
    def is_winners_reveal_date_passed(self):
        today = timezone.now().date()
        return today >= self.winners_reveal_date

    class Meta:
        verbose_name = 'Site Parameters'
        verbose_name_plural = 'Site Parameters'
