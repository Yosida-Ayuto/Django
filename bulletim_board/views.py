from django.shortcuts import render
from django.views import generic
from .models import bulletim_board
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import bulletim_boardCreateForm
from django.contrib import messages
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class Bulletim_boardListView(LoginRequiredMixin, generic.ListView):
    model = bulletim_board
    template_name = 'list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = bulletim_board.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


class Bulletim_boardCreateView(LoginRequiredMixin, generic.CreateView):
    model = bulletim_board
    template_name = 'create.html'
    form_class = bulletim_boardCreateForm
    success_url = reverse_lazy('bulletim_board:list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '投稿に成功しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿に失敗しました。")
        return super().form_invalid(form)

# 2022/9/29
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = bulletim_board
    template_name = 'update.html'
    form_class = bulletim_boardCreateForm

    def get_success_url(self):
        return reverse_lazy('bulletim_board:list', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新に失敗しました。")
        return super().form_invalid(form)