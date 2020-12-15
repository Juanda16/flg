"""flgApp URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import userView

router = routers.DefaultRouter()
router.register(r'donors', userView.DonorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.routes.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', include(router.urls))
]
