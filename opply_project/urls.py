from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authentication import TokenAuthentication
from rest_framework.routers import DefaultRouter

from customer.views import CustomerViewSet
from product.views import ProductViewSet
from order.views import OrderViewSet
from auth_app.views import CustomAuthToken
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'customers', CustomerViewSet, basename='customer')

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Your API description",
    ),
    public=True,
    authentication_classes=[TokenAuthentication],
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth-token/', CustomAuthToken.as_view(), name='auth-token'),

    # Swagger endpoints
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI
]
