from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api import views

urlpatterns = {
    url(r'^pkls/$', views.parking),
    url(r'^pklsd/((?P<olat>\d+(?:\.\d+)?)&&(?P<olongt>\d+(?:\.\d+)?)K(?P<km>[0-9]+))$',views.parking_distance),
    url(r'^users/$', views.users),
    url(r'^usersp/', views.users_pk),
    url(r'^bookings/$', views.bookings),
    url(r'^bookingsu/(?P<userid>[0-9]+)$', views.bookings_user),
    url(r'^rateds/$', views.ratings),
}

urlpatterns = format_suffix_patterns(urlpatterns)