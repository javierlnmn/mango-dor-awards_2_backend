from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserProfileView,
    CustomTokenObtainPairView,
    LogoutView
)

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # JWT token endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 