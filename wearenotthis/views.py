from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Supporter


class HomeView(TemplateView):

    def get(self, request, **kwargs):

        template = 'index.html'

        supporter_count = Supporter.objects.count()

        supporters = Supporter.objects.all()

        context = {
            'supporter_count': supporter_count,
            'supporters': supporters
        }

        return render(request, template, context)
