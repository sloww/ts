from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<num>\d{4,9})/$', views.get_deal, name='get_deal'),
]
