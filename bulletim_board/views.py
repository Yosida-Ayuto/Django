from django.shortcuts import render
from django.views import generic
from .models import bulletim_board
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import bulletim_boardCreateForm
from django.contrib import messages
# Create your views here.
# 追加

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
        diary = get_object_or_404(bulletim_board, pk=self.kwargs['pk'])
        # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
        return self.request.user == bulletim_board.user



class IndexView(generic.TemplateView):
    template_name = "index.html"

class Bulletim_boardListView(LoginRequiredMixin, generic.ListView):
    model = bulletim_board
    template_name = 'list.html'
    paginate_by = 10

    def get_queryset(self):
        diaries = bulletim_board.objects.order_by('-created_at')
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

# 2022/9/29アップデート追加
class UpdateView(LoginRequiredMixin, OnlyYouMixin,generic.UpdateView):
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
# 2022/9/29デリート追加

class DeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = bulletim_board
    template_name = 'delete.html'
    success_url = reverse_lazy('bulletim_board:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)

# 9/29詳細
class DetailView(LoginRequiredMixin, generic.DetailView):
    model = bulletim_board
    template_name = 'detail.html'