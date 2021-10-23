from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/',      admin.site.urls),
    path(r'',           include('apps.base.urls')),
    path(r'polls/',     include('apps.polls.urls')),
    path(r'tutorials/', include('tutorials.urls')),
]
