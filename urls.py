from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<num>\d{5,13})/$', views.get_deal, name='get_deal'),
]
