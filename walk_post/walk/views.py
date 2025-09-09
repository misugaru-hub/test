from django.views.generic import ListView

from .models import Walk

class WalkListView(ListView):
    model = Walk

