from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from utils.views import redirect_to_admin


urlpatterns = [
    path('', redirect_to_admin),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('blog/', include('saq.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)