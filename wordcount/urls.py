#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('kells/', admin.site.urls),
    path('', views.homepage, name='home' ),
    path('mgk/', views.mgk),
    path('count/', views.count, name='count'),
    path('about/', views.about,  name='about'),
]
