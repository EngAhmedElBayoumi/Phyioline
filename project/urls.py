"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#import settings and static and media
from django.conf import settings
from django.conf.urls.static import static

# localization
from django.conf.urls.i18n import i18n_patterns
from .api import get_dashboard_stats, get_chart_data



urlpatterns = [
    path("admin/", admin.site.urls),
    path('dashboard_stats/', get_dashboard_stats, name='dashboard_stats'),
    path('chart_data/', get_chart_data, name='chart_data'),
    path('i18n/', include('django.conf.urls.i18n')),  # Add this line for language switching

    
]
# URLs with language prefix
urlpatterns += i18n_patterns(
    path("", include("home.urls")),
    path("account/", include("account.urls")),
    path("product/", include("product.urls")),
    prefix_default_language=True
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)