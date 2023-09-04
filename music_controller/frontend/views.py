from django.shortcuts import render

# Create your views here.
# This allows react to take over and inject content


def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
