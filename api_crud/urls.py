
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# urls
urlpatterns = [
    path('api/roran-williams/blogs/', include('blogs.urls')),
    path('api/roran-williams/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)