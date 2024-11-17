from datetime import date
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Produto


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        validade = request.POST.get('validade')
        quantidade = request.POST.get('quantidade')

        if nome and validade:
            Produto.objects.create(
                nome=nome,
                validade=validade,
                quantidade=quantidade,
            )

        return redirect('index')

    produtos = Produto.objects.filter(removido_em__isnull=True).order_by('validade')
    hoje = date.today()

    return render(request, 'core/index.html', {
        'hoje': hoje,
        'produtos': produtos,
    })


def remover(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if not produto.removido:
        produto.removido_em = date.today()
        produto.save()

    return redirect('index')
