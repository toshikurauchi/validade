from datetime import date, timedelta
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


def define_quantidade(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    is_first = request.GET.get('is_first') == 'True'
    is_last = request.GET.get('is_last') == 'True'

    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade'))

        if 0 < quantidade:
            produto.quantidade = quantidade
            produto.save()

    return render(request, 'core/partials/produto.html', {'produto': produto, 'is_first': is_first, 'is_last': is_last})


def aumenta_quantidade(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    is_first = request.GET.get('is_first') == 'True'
    is_last = request.GET.get('is_last') == 'True'

    if not produto.removido:
        produto.quantidade += 1
        produto.save()

    return render(request, 'core/partials/produto.html', {'produto': produto, 'is_first': is_first, 'is_last': is_last})


def diminui_quantidade(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    is_first = request.GET.get('is_first') == 'True'
    is_last = request.GET.get('is_last') == 'True'

    if not produto.removido and produto.quantidade > 1:
        produto.quantidade -= 1
        produto.save()

    return render(request, 'core/partials/produto.html', {'produto': produto, 'is_first': is_first, 'is_last': is_last})


def remover(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if not produto.removido:
        produto.removido_em = date.today()
        produto.save()

    return redirect('index')
