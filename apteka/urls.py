from django.urls import path
from apteka.models import Check
from apteka.views import ReportView

urlpatterns = [
    path('report/', ReportView.as_view(), name='view'),
]
