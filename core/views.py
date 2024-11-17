from datetime import date
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Produto, Tag


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
        'current_page': 'home',
        'hoje': hoje,
        'produtos': produtos,
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


def lista_tags(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        if nome:
            Tag.objects.create(nome=nome)

        return redirect('tags')

    tags = Tag.objects.all()

    return render(request, 'core/tags.html', {
        'current_page': 'tags',
        'tags': tags,
    })


def deleta_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tag.delete()

    return redirect('tags')
