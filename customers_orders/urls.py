from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CustomerViewSet, OrderViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponseRedirect

# Set up the schema view for Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Customers and Orders API",
      default_version='v1',
      description="API documentation for managing customers and orders",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Set up the router for your viewsets
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

# Define the URL patterns
urlpatterns = [
    # Redirect root URL to swagger
    path('', lambda request: HttpResponseRedirect('/swagger/')),

    # Admin and API routes
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
