from django.shortcuts import redirect, reverse, get_object_or_404, render
from django.views.generic import View, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.contrib.auth import login, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages

from apps.core.utils import toast_form_errors, validate_form
from apps.notification.models import Notification
from apps.notification.utils import create_notify_for_admins
from apps.ticket.models import Ticket
from apps.course.models import Course
from .mixinx import LogoutRequiredMixin
from .models import User
from . import forms
from random import randint


# Render Login view
class LoginView(LogoutRequiredMixin, FormView):
    template_name = 'account/signin.html'
    form_class = forms.LoginForm
    success_url = '/'

    def remember_me(self, form):
        remember_me = form.cleaned_data.get('remember_me', False)
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

    def form_valid(self, form):
        user = form.cleaned_data.get('user')

        # Redirect to phone verification if user is not verified
        if not user.is_verified:
            token = user.generate_token()
            self.request.session['secret_token'] = token

            return redirect('account:send_code')

        # Login user and set session expiry time
        login(self.request, user=user)
        self.remember_me(form)

        messages.success(self.request, _('Login successful'))
        return super().form_valid(form)

    def form_invalid(self, form):
        toast_form_errors(self.request, form)
        return super().form_invalid(form)


# Render Register view
class RegisterView(LogoutRequiredMixin, FormView):
    template_name = 'account/signup.html'
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('account:send_code')


    def form_valid(self, form):
        user = form.save()

        # Create register token and save it in sessions
        token = user.generate_token()
        self.request.session['secret_token'] = token
        create_notify_for_admins('NEW_USER_ADMIN', _('A new user has been registered'))
        return super().form_valid(form)

    def form_invalid(self, form):
        toast_form_errors(self.request, form)
        return super().form_invalid(form)


# SendCode view
class SendCodeView(LogoutRequiredMixin, View):
    def get_redirect_url(self):
        next_url = self.request.GET.get('next', reverse('account:verify_phone'))
        return next_url

    def get(self, request):
        code = randint(10000, 99999)
        request.session['verify_code'] = code

        token = request.session.get('secret_token')
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            messages.error(request, _('There is an issue! please try again'))
            return redirect('account:register')

        Notification.objects.create(
            type=Notification.TYPES.MOBILE_VERIFICATION_CODE,
            title=_('Phone number verification code'),
            kwargs={'code': code},
            to_user=user,
            send_notify=True
        )

        messages.info(request, _('Code sent to you'))
        return redirect(self.get_redirect_url())

# Render VerifyPhoneNumber view
class VerifyPhoneNumberView(LogoutRequiredMixin, FormView):
    template_name = 'account/verify_phone.html'
    form_class = forms.VerifyPhoneNumberForm
    success_url = reverse_lazy('')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if self.request.method == 'POST':
            kwargs['data'] = {
                'code': self.request.POST.get('code'),
                'verify_code': self.request.session.get('verify_code'),
                'token': self.request.session.get('secret_token')
            }

        return kwargs

    def form_valid(self, form):
        user = form.cleaned_data.get('user')

        # Verify user and clear token
        user.is_verified = True
        user.clear_token(self.request)
        login(self.request, user)

        # Delete code from session
        if 'verify_code' in self.request.session:
            del self.request.session['verify_code']

        messages.success(self.request, _('Register done successful'))
        return redirect('public:welcome')

    def form_invalid(self, form):
        toast_form_errors(self.request, form)
        return super().form_invalid(form)


# GetPhoneNumber view
class GetPhoneNumberView(LogoutRequiredMixin, FormView):
    template_name = 'account/password/get_phone.html'
    form_class = forms.GetPhoneNumberForm

    def get_success_url(self):
        return reverse('account:send_code') + f'?next={reverse("account:reset_pass_confirm")}'

    def form_valid(self, form):
        user = form.cleaned_data.get('user')

        # Create register token and save it in sessions
        token = user.generate_token()
        self.request.session['secret_token'] = token

        return super().form_valid(form)

    def form_invalid(self, form):
        toast_form_errors(self.request, form)
        return super().form_invalid(form)


# ResetPasswordConfirm view
class ResetPassConfirmView(LogoutRequiredMixin, FormView):
    template_name = 'account/password/reset_pass_confirm.html'
    form_class = forms.VerifyPhoneNumberForm
    success_url = reverse_lazy('account:reset_pass_complete')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if self.request.method == 'POST':
            kwargs['data'] = {
                'code': self.request.POST.get('code'),
                'verify_code': self.request.session.get('verify_code'),
                'token': self.request.session.get('secret_token')
            }

        return kwargs

    def form_valid(self, form):
        # Delete code from session
        if 'verify_code' in self.request.session:
            del self.request.session['verify_code']

        return super().form_valid(form)

    def form_invalid(self, form):
        toast_form_errors(self.request, form)
        return super().form_invalid(form)


# ResetPasswordComplete view
class ResetPassCompleteView(LogoutRequiredMixin, FormView):
    template_name = 'account/password/reset_pass_complete.html'
    form_class = forms.ResetPassForm
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        password = form.cleaned_data.get('password2')
        token = self.request.session.get('secret_token')

        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            messages.error(self.request, _('There is an issue! please try again'))
            return self.form_invalid(form)

        # Set new password and clear tokens
        user.set_password(password)
        user.is_verified = True
        user.clear_token(self.request)

        messages.success(self.request, _('Password successfully reset'))
        return super().form_valid(form)

    def form_invalid(self, form):
        toast_form_errors(self.request, form)
        return super().form_invalid(form)


# UserProfile view
class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['ticket_count'] = Ticket.objects.filter(user=user).count()
        context['course_count'] = Course.objects.filter(user=user).count()
        return context

    def get(self, request):
        form = forms.UpdateProfileForm(instance=request.user.profile, initial={
            'phone_number' : request.user.phone_number,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name
        })
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = forms.UpdateProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if validate_form(request, form):
            form.save()

            messages.success(request, _('Profile updated successfully'))
            return redirect('account:profile_details')

        return render(request, self.template_name, {'form':form})


# EditPassword view
class EditPasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.CustomPasswordChangeForm(user=request.user)
        return render(request, 'account/password/edit_password.html', {'form': form})

    def post(self, request):
        form = forms.CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Password changed successfully'))
            return redirect('account:profile_details')
        else:
            messages.error(request, _('Please correct the error below.'))
        return render(request, 'account/password/edit_password.html', {'form': form})