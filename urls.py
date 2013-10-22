from django.conf.urls import patterns, include, url

from django_type_rel.views import Items


urlpatterns = patterns('',
                       url(r'dtr/listing', Items.as_view(),name = "dtr_listing"),
)

