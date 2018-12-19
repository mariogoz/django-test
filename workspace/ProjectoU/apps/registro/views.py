from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.

def index(request):
    
    form = PostForm()
    return render(request, 'registro/index.html', {'form': form})