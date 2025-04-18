from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from azbankgateways.urls import az_bank_gateways_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('accounts/', include('apps.account.urls', namespace='account')),
    path('', include('apps.public.urls', namespace='public')),
    path('customers/', include('apps.customers.urls', namespace='customers')),
    path('subscription/', include('apps.subscription.urls', namespace='subscription')),
    path('payment/', include('apps.payment.urls', namespace='payment')),
    path('course/', include('apps.course.urls', namespace='course')),
    path('ticket/', include('apps.ticket.urls', namespace='ticket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)