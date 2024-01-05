from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from store_app import views


urlpatterns = format_suffix_patterns([
    
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]