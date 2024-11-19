from django.db.models import Q

from core.models import Produto


def produtos_filtrados(request):
    q = request.GET.get('q', '').strip()

    prefix = 'tag--'
    tags_selecionadas = [param[len(prefix):] for param in request.GET if param.startswith(prefix)]

    produtos = Produto.objects.filter(removido_em__isnull=True, nome__icontains=q)
    if tags_selecionadas:
        filtro = None
        for tag in tags_selecionadas:
            if filtro:
                filtro = filtro | Q(tags__nome=tag)
            else:
                filtro = Q(tags__nome=tag)
        produtos = produtos.filter(filtro)

    return produtos.order_by('validade'), tags_selecionadas
