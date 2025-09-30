from django.views.generic import (ListView ,CreateView,
                                  DetailView,UpdateView,DeleteView)
from walk.forms import WalkForm
from .models import Walk
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class StaffroomMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")

class WalkListView(ListView):
    model = Walk

class PostCreateView(StaffroomMixin,CreateView):
    model = Walk
    form_class = WalkForm
    success_url = reverse_lazy("index")
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.POST.dict()
        data['user'] = user.id
        form = WalkForm(data=data, files=request.FILES)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存できませんでした")
        return super().form_invalid(form)
   
class PostDetailView(DetailView):
    model = Walk

class PostUpdateView(StaffroomMixin,UpdateView):
    model = Walk
    fields = ["weather", "steps", "startpoint","endpoint","content","image", ]
    success_url = "/"
   
class PostDeleteView(StaffroomMixin,DeleteView):
    model = Walk
    success_url = "/"
def index(request):
    
    walklist = Walk.objects.all()
    
    return render(request, 'walk/map.html',{'walklist': walklist})
    


