from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('product', ProductViewSet, basename='products')
router.register('news', NewsViewSet, basename='car')
router.register('register', RegisterViewSet, basename='register')
router.register('newaccount', NewAccountViewSet, basename='newaccount')
router.register('money', MoneyViewSet, basename='money')
router.register('advertsiment', AdvertsimentViewSet, basename='advertsiment')
router.register('discount', DiscountViewSet, basename='discount')
router.register('sale', SaleViewSet, basename='sale')
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

