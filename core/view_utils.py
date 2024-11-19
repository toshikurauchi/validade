from core.models import Produto


def produtos_filtrados(request):
    q = request.GET.get('q', '').strip()
    print('Q', q)
    return Produto.objects.filter(removido_em__isnull=True, nome__icontains=q).order_by('validade')
