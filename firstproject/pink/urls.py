from django.urls import path
from . import views

urlpatterns = [
    path('', views.pink_page, name='pink_page'),
]
