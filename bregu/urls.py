
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home and About Page
    path('', include('pages.urls')),
    # Listings
    path('listings/', include('listings.urls')),
    # Admin page
    path('admin/', admin.site.urls),
    # contact
    path('contact/', include('contact.urls')),
    # blog
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
