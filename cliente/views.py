from django.shortcuts import redirect, render

from .models import Cliente


def index_cliente(request):
    return render(request, 'cliente/index.html')


def cliente_listar(request):
    clientes = Cliente.objects.all().order_by('-fecha_registro')
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})


def cliente_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        telefono = request.POST.get('telefono', '').strip()

        if nombre and email:
            Cliente.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
            )
            return redirect('cliente_listar')

    return render(request, 'cliente/formulario_cliente.html', {'cliente': None})