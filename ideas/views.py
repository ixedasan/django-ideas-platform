from django.shortcuts import render, redirect
from ideas.models import Ideas, Comments
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from ideas.forms import CommentsForm, IdeasForm


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'index.html')


@login_required
def home(request):
    ideas = Ideas.objects.all()
    return render(request, 'ideas/home.html', {'ideas': ideas})


@login_required
def idea_detail(request, pk):
    idea = get_object_or_404(Ideas, pk=pk)
    comments = Comments.objects.filter(idea=idea)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.idea = idea
            comment.user = request.user
            comment.save()
            return redirect('idea_detail', pk=pk)
    else:
        form = CommentsForm()
    context = {
        'idea': idea,
        'comments': comments,
        'form': form
    }
    return render(request, 'ideas/idea_detail.html', context)


@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeasForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            return redirect('home')
    else:
        form = IdeasForm()
    return render(request, 'ideas/operations/idea_create.html', {'form': form})


@login_required
def idea_update(request, pk):
    idea = get_object_or_404(Ideas, pk=pk)
    if request.user.id != idea.user_id:
        return redirect('home')
    if request.method == 'POST':
        form = IdeasForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IdeasForm(instance=idea)
    return render(request, 'ideas/operations/idea_update.html', {'form': form})


@login_required
def idea_delete(request, pk):
    idea = get_object_or_404(Ideas, pk=pk)
    if request.user.id != idea.user_id:
        return redirect('home')
    if request.method == 'POST':
        idea.delete()
        return redirect('home')
    return render(request, 'ideas/operations/idea_delete.html', {'idea': idea})
