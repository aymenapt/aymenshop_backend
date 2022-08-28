
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/Singnup/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('product.urls')),
    path('api/v1/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
