from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers


# for ModelViewSet

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'_profiles', views.ProfileViewSet)
router.register(r'orders', views.OrderViewSet, basename='orders')

product_router = routers.NestedDefaultRouter(router, r'products', lookup='productt')
product_router.register(r'reviews', views.ReviewViewSet, basename='product-reviews')

cart_router = routers.NestedDefaultRouter(router, r'carts', lookup='cartt')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')



# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
]


# for Class-based views and Generics views

# urlpatterns = [
    # path('products/', views.ApiProducts.as_view()),
    # path('products/<str:pk>', views.ApiProduct.as_view()),
    # path('categories/', views.ApiCategories.as_view()),
    # path('categories/<str:pk>', views.ApiCategory.as_view()),
# ]


# for api_views

# urlpatterns = [
    # path('products/', views.ApiProducts),
    # path('products/<str:pk>', views.ApiProduct),
    # path('categories/', views.ApiCategories),
    # path('categories/<str:pk>', views.ApiCategory),
# ]