from django.db.models import Q, Count
from django.shortcuts import get_object_or_404

from core.models import Produto, Tag


def produtos_filtrados(request):
    q = request.GET.get('q', '').strip()

    prefix = 'tag--'
    tags_selecionadas = [param[len(prefix):] for param in request.GET if param.startswith(prefix)]

    produtos = Produto.objects.filter(removido_em__isnull=True, nome__icontains=q)
    for tag in tags_selecionadas:
        produtos = produtos.filter(tags__nome=tag)

    return produtos.order_by('validade'), tags_selecionadas


def salva_ou_atualiza_produto(request):
    produto = None
    produto_id = request.POST.get('produto_id')
    nome = request.POST.get('nome')
    validade = request.POST.get('validade')
    quantidade = request.POST.get('quantidade')
    tags = []

    tag_i = 0
    while True:
        tag = request.POST.get(f'tag-{tag_i}')
        if tag:
            tags.append(get_object_or_404(Tag, nome=tag))
            tag_i += 1
        else:
            break

    if nome and validade:
        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            produto.nome = nome
            produto.validade = validade
            produto.quantidade = quantidade
        else:
            produto = Produto.objects.create(
                nome=nome,
                validade=validade,
                quantidade=quantidade,
            )
        produto.tags.set(tags)
        produto.save()

    return Produto.objects.get(pk=produto.id)
