from django.shortcuts import render
from django.views import generic
from .models import bulletim_board
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class Bulletim_boardListView(LoginRequiredMixin, generic.ListView):
    model = bulletim_board
    template_name = 'bulletim_bord_list'
    paginate_by = 2

    def get_queryset(self):
        diaries = bulletim_board.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries
