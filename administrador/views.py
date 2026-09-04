from django.shortcuts import render

def index_admin(request):
    return render(request, 'administrador/index.html')