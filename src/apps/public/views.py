from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.course.models import Course, CourseCategory
from .models import IndexVideo, TopBanner


# Render Index view
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'courses': Course.objects.filter(is_active=True).order_by('-id')[:4],
            'categories': CourseCategory.objects.all(),
            #'banners': TopBanner.objects.filter(is_active=True),
            #'index_videos': IndexVideo.objects.filter(is_active=True),
        })

        return context


class WelcomeView(TemplateView):
    template_name = 'public/welcome.html'


class test(TemplateView):
    template_name = 'ticket/ticket_details.html'
