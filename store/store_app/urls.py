from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from store_app import views


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('product/',
        views.ProductList.as_view(),
        name='product-list'),
    path('product/<int:pk>/',
        views.ProductDetail.as_view(),
        name='product-detail'),
    path('category/',
        views.CategoryList.as_view(),
        name='category-list'),
    path('category/<int:pk>/',
        views.CategoryDetail.as_view(),
        name='category-detail'),
    path('seller/',
        views.SellerList.as_view(),
        name='seller-list'),
    path('seller/<int:pk>/',
        views.SellerDetail.as_view(),
        name='seller-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]