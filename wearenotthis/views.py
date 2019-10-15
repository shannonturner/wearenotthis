from django.views.generic import ListView
from .models import Supporter

class HomeView(ListView):
    model = Supporter
