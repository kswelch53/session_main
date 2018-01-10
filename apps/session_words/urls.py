#app-level url code:
from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^addword$', views.addword),
    url(r'^displayword$', views.displayword),
    url(r'^clear$', views.clear),
]
