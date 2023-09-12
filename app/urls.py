from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api_schema' ),
    
    path('api/docs/', 
        SpectacularSwaggerView.as_view(url_name="api_schema"), name="api_docs"),
    path('api/users/', include('user.urls'), name = 'users')
]
