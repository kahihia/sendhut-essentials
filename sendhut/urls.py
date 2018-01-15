from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib import admin

from sendhut.lunch import urls as lunch_urls
from sendhut.accounts import urls as account_urls
from sendhut.dashboard import urls as dashboard_urls
from sendhut.accounts.views import LoginView, LogoutView, SignupView
from sendhut.lunch.views import join_group_order
from .views import (
    home, about, faqs, privacy_terms,
    payment_callback, payment_webhook
)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about-us/$', about, name='about-us'),
    url(r'^faqs/$', faqs, name='faqs'),
    url(r'^privacy_terms/$', privacy_terms, name='privacy-terms'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='signin'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^accounts/', include(account_urls, namespace='accounts')),
    # group order join
    url(r'^g/(?P<name>[a-zA-Z0-9-]+)/$', join_group_order,
        name='group_order_join'),
    # payment transaction callback
    url(r'^payments/ck$', payment_callback, name='payment_callback'),
    # instant payment notification
    url(r'^payments/ipn$', payment_webhook, name='payment_webhook'),
    # password reset
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^lunch/', include(lunch_urls, namespace='lunch')),
    url(r'^business/', include(dashboard_urls, namespace='dashboard')),
    url(r'^admin/', include(admin.site.urls)),

]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
