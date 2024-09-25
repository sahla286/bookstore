from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('api/books',views.ProductViewsetView,basename='books')
router.register('users',views.UserViewsetView,basename='users')
router.register('cart',views.CartView,basename='cart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/<int:id>/', views.ReviewView.as_view()),
] +router.urls

