from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("api/v1/", include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),  # new
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path('csrf_token/', views.get_csrf_token, name='get_csrf_token'),
]
