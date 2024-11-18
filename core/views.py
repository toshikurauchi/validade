from datetime import date
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Produto, Tag


def index(request):
    if request.method == 'POST':
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
            Produto.objects.create(
                nome=nome,
                validade=validade,
                quantidade=quantidade,
            ).tags.set(tags)

        return redirect('index')

    produtos = Produto.objects.filter(removido_em__isnull=True).order_by('validade')
    hoje = date.today()

    return render(request, 'core/index.html', {
        'current_page': 'home',
        'hoje': hoje,
        'produtos': produtos,
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

    return redirect('index')


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
