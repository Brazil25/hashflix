from .models import Filme


def filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}

def filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"filmes_em_alta": lista_filmes}