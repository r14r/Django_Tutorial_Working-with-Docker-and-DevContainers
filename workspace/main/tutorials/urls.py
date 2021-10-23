from django.urls import include, path

app_name = 'tutorials'

urlpatterns = [
    path(r'rest/', include('tutorials.rest.urls')),
]
