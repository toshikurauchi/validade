from django.shortcuts import get_object_or_404, render

from core.models import Produto


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
