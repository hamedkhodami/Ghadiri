from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect


from apps.account.forms import UpdateProfileForm
from apps.notification.models import Notification
from apps.notification.utils import create_notify_for_admins
from . import forms, models



# Add Counseling
class CounselingAddView(LoginRequiredMixin, TemplateView):
    template_name = 'customers/counseling/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['Counseling'] = models.Counseling
        return context

    def get_redirect_url(self):
        referer_url = self.request.META.get('HTTP_REFERER')
        return referer_url

    def post(self, request):
        data = self.request.POST.copy()
        work_shifts = ' | '.join(data.getlist('work_shift', []))
        data['work_shift'] = work_shifts

        user = request.user
        if not user.is_profile_completed:
            form_user = UpdateProfileForm(data, instance=user.profile)
            if not form_user.is_valid():
                messages.error(self.request, _('Please enter fields correctly'))
                return redirect(self.get_redirect_url())
            form_user.save()

        form = forms.CounselingForm(data, files=self.request.FILES)
        if not form.is_valid():
            messages.error(self.request, _('Please enter fields correctly'))
            return redirect(self.get_redirect_url())
        obj = form.save()
        # create notification for admin's
        create_notify_for_admins(
            Notification.TYPES.NEW_COUNSELING_FORM_SUBMITED_ADMIN,
            _('New counseling form submited')
        )
        messages.success(self.request, _('Your counseling form has been successfully submited'))
        return redirect(self.get_redirect_url())

from django.shortcuts import render

# Create your views here.
