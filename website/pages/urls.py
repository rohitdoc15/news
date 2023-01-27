from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('afterclick/', views.click , name='click')

]

htmx_url_patterns = [
         path('check_channel/', views.check_channel , name='check_channel'),
         path('searchlist/', views.check_channel , name='searchlist'),
]


urlpatterns += htmx_url_patterns