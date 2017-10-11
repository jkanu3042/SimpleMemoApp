from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import Memo
from .forms import MemoCreateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def memo_list(request):
    memo_qs = Memo.objects.all()
    paginator = Paginator(memo_qs, 9)

    page = request.GET.get('page',1)

    try:
        memo_lst = paginator.page(page)
    except PageNotAnInteger:
        memo_lst = paginator.page(1)
    except EmptyPage:
        memo_lst = paginator.page(paginator.num_pages)


    return render(request, 'post/memo_list.html', {
        'memo_list': memo_lst,
    })

class MemoCreateView(CreateView):
    model = Memo
    form_class = MemoCreateForm

memo_create = MemoCreateView.as_view()


class MemoDetailView(DetailView):
    model = Memo

memo_detail = MemoDetailView.as_view()



