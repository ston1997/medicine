from django.shortcuts import render
from django.views.generic import ListView
from apteka.models import PositionCheck, Check


# Create your views here.
class ReportView(ListView):
    model = Check
    template_name = 'apteka/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)
        return context
