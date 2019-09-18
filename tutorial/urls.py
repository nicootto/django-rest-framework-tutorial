from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browsable API.
urlpatterns = [
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
