from datetime import date
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Produto, Tag
from core.view_utils import produtos_filtrados


def lista_produtos(request):
    produtos = produtos_filtrados(request)

    return render(request, 'core/produtos.html', {
        'current_page': 'produtos',
        'produtos': produtos,
        'tags': Tag.objects.all(),
    })


def cadastro(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        nome = request.POST.get('nome')
        validade = request.POST.get('validade')
        quantidade = request.POST.get('quantidade')
        origem = request.POST.get('origem')
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

        return redirect(origem)

    return render(request, 'core/cadastro.html', {
        'current_page': 'cadastro',
        'tags': Tag.objects.all(),
    })


def historico(request):
    produtos = Produto.objects.filter(removido_em__isnull=False).order_by('-removido_em')

    return render(request, 'core/historico.html', {
        'current_page': 'historico',
        'produtos': produtos,
    })


def remover(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if not produto.removido:
        produto.removido_em = date.today()
        produto.save()

    return redirect('lista-produtos')


def restaurar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if produto.removido:
        produto.removido_em = None
        produto.save()

    return redirect('historico')


def lista_tags(request, tag_id=None):
    tag = None
    if tag_id:
        tag = Tag.objects.get(pk=tag_id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cor_fundo = request.POST.get('cor_fundo')
        cor_texto = request.POST.get('cor_texto')

        if nome:
            if tag:
                tag.nome = nome
                tag.cor_fundo = cor_fundo
                tag.cor_texto = cor_texto
            else:
                tag = Tag(nome=nome, cor_fundo=cor_fundo, cor_texto=cor_texto)
            tag.save()

        return redirect('tags')

    tags = Tag.objects.all()

    return render(request, 'core/tags.html', {
        'current_page': 'tags',
        'tags': tags,
        'tag': tag,
    })


def deleta_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tag.delete()

    return redirect('tags')
