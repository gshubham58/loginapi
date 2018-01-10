from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^user=(?P<ud>[a-z]+)&pwd=(?P<pd>([a-z])+)/$',views.add,name='add'),
]
