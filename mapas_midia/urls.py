from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^index/', TemplateView.as_view(template_name="index.html")),
        url(r'^admin/', include(admin.site.urls)),
)
