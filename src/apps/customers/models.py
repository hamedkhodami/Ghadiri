from django.utils.translation import gettext as _
from django.db import models

from .enums import ActivityFieldsTypeEnum,WorkShiftsTypeEnum,YesOrNoTypeEnum


class Counseling(models.Model):

    user = models.ForeignKey('account.User', on_delete=models.CASCADE, verbose_name=_('User'))
    field_of_activity = models.CharField(max_length=25, choices=ActivityFieldsTypeEnum.choices, verbose_name=_('Field of Activity'))
    work_experience = models.CharField(max_length=20, verbose_name=_('Work Experience'))
    work_shift = models.CharField(max_length=50, verbose_name=_('Work Shift'), null=True, blank=True)
    number_of_staff = models.IntegerField(_('Number of staff'))
    capacity = models.IntegerField(_('Capacity'))
    personnel_training = models.TextField(null=True, blank=True, verbose_name=_('Personnel Training Detail'))

    class Meta:
        verbose_name = _('Counseling')
        verbose_name_plural = _('Counselings')
from django.db import models

# Create your models here.
