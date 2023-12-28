from django.contrib import admin
from django.urls import path
from .views import weblog, coba2
urlpatterns= [
    path('admin/', admin.site.urls),
    path('',weblog , name='weblog'),
    path('coba2/', coba2, name='coba2'),
]