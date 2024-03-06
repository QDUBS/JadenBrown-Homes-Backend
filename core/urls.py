
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (SpectacularAPIView,
                                    SpectacularRedocView, 
                                    SpectacularSwaggerView)

urlpatterns = [
    path('admin/', admin.site.urls),

    # EMAIL DESIGN TEMPLATE VIEW
    path("templates/", include("templates.url")),

    #  USER PROFILES AND AUTH VIEWS
    path("api/auth/", include("routes.auth")),
    path("api/user/profile/", include("routes.profile")),

    # GENERAL LISTINGS VIEW
    path("api/listings/", include("routes.houses")),
    path("api/listings/properties/", include("routes.properties")),

    # DASHBOARD URLS
    path("api/dashboard/", include("routes.dashboard")),
    
    # SWAGGER SPECTACULAR DOCS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

if  settings.DEBUG:
    urlpatterns+=[
    path("__debug__/", include("debug_toolbar.urls")),

    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
