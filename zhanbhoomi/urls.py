from django.contrib import admin
from django.urls import path
from scedule.views import teenager_application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',teenager_application,name='teenager_form'),
]
