from django.urls import path

from .views import SiteParametersView

urlpatterns = [
    path('site-parameters/', SiteParametersView.as_view(), name='site-parameters'),
]
