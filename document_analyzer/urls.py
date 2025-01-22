from django.contrib import admin
from django.urls import path
from analyzer import views
from django.views.generic.base import RedirectView

urlpatterns = [
        path('', RedirectView.as_view(url='upload/', permanent=False), name='index'),
    path('admin/', admin.site.urls),
    path('upload/', views.upload_document, name='upload_document'),
]
