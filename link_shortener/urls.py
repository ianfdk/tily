from django.conf.urls import url

from . import views

app_name = 'link_shortener'
urlpatterns = [
    url(r'^$', views.index,
        name='index'),
    url(r'^(?P<tiny_url>([a-zA-Z]|[0-9]|[$-_@.&+])+)$', views.redirection,
        name='redirection'),
]
