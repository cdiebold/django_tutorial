from django.conf.urls import import url
from . import import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
