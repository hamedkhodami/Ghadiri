from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('counseling/add', views.CounselingAddView.as_view(), name='counseling_add'),
]
