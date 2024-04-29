from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FormulasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'formulas'
    verbose_name = _('Formulas')
