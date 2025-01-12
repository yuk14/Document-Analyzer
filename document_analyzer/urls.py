from django.contrib import admin
from django.urls import path
from analyzer import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
        path('', RedirectView.as_view(url='upload/', permanent=False), name='index'),
    path('admin/', admin.site.urls),
    path('upload/', views.upload_document, name='upload_document'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)