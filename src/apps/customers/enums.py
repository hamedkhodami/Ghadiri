from django.utils.translation import gettext as _
from django.db.models import TextChoices


class ActivityFieldsTypeEnum(TextChoices):
    CATERING = 'catering', _('Catering')
    OTHER = 'other', _('Other')


class WorkShiftsTypeEnum(TextChoices):
    MORNING = 'morning ', _('Morning')
    NOON = 'noon ', _('Noon')
    NIGHT = 'night ', _('Night')


class YesOrNoTypeEnum(TextChoices):
    YES = 'yes ', _('Yes')
    NO = 'no ', _('No')
