from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BoardModel

def index(request):
    return render(request, 'boardapp/index.html')

def list(request):
    
    boardmodel_list = BoardModel.objects.all()
    return render(
        request,
        'boardapp/list.html',
        {
            'boardmodel':boardmodel_list
        }
    )
    
def add(request):
    if request.method == 'GET':
        return render(request, 'boardapp/add.html')
    else:
        title = request.POST['title']
        writer = request.POST['writer']
        content = request.POST['content']
        BoardModel(title=title, writer=writer, content=content).save()
        return HttpResponseRedirect(reverse('board:list'))
    
def detail(request):
    id =request.GET['id']
    boardmodel = BoardModel.objects.get(id=id)
    boardmodel.incrementReadCount()
    return render(request, 'boardapp/detail.html',
                {'boardmodel':boardmodel}
    )
    
def edit(request):
    id = request.GET['id']
    boardmodel = BoardModel.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'boardapp/edit.html',
                    {'boardmodel':boardmodel}
    )
    elif request.method == 'POST':
        boardmodel.title = request.POST['title']
        boardmodel.writer = request.POST['writer']
        boardmodel.content = request.POST['content']
        boardmodel.save()
        return HttpResponseRedirect(reverse('board:detail'))

def delete(request):
    id = request.GET['id']
    boardmodel = BoardModel.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'boardapp/delete.html',
                    {'boardmodel':boardmodel}
    )
    elif request.method == 'POST':
        boardmodel.delete()
        return HttpResponseRedirect(reverse('board:list'))
        