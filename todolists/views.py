from django.shortcuts import get_object_or_404, render, redirect

from .forms import TodoListForm
from .models import TodoList


def home(request):
    if request.user.is_authenticated():
        return redirect('todolists:show_lists')
    return render(request, 'todolists/home.html')


def new_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            new_list = TodoList()
            new_list.title = form.cleaned_data['title']
            new_list.description = form.cleaned_data['description']
            new_list.is_active = True
            new_list.user = request.user
            new_list.save()
            return redirect('todolists:show_lists')
    else:
        form = TodoListForm()
    return render(request, 'todolists/new_list.html', {'form': form})


def show_lists(request, category=None):
    todolists = TodoList.objects.filter(is_active=True, user=request.user)
    return render(request, 'todolists/show_lists.html', {'todolists': todolists})


def list_detail(request, pk):
    list = get_object_or_404(TodoList, pk=pk)
    return render(request, 'todolists/list_detail.html', {'list': list})