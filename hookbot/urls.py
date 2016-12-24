from django.conf.urls import url, include
from django.contrib import admin
from app.views import PayloadView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^payload', PayloadView.as_view())
]
