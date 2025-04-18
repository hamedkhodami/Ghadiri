from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class TicketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ticket'
    verbose_name = _('Ticket')

    def ready(self):
        from . import signals