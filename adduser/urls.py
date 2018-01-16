from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^user=(?P<ud>[^/]+)&pwd=(?P<pd>([^/])+)/$',views.add,name='add'),


]
