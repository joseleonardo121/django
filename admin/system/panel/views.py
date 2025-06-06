from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum
from .models import Tareas,ConjuntosLicraDama,ConjuntosNovaDama,ConjuntosInterfilDama,ConjuntosElasticDama,ConjuntosFranelaDama,ConjuntosTelaMojadaDama,ConjuntosPlushDama,ConjuntosPoliesterDama,ConjuntosPolifreshDama,ConjuntosLomaDama,ConjuntosBosseDama,ConjuntosTerryDama,ConjuntosFranelaPLushDama,ConjuntosCortavientoReversibleDama
from .models import (
    ConjuntosCortavientoReversibleVaron,
    ConjuntosCortavientoVaron,
    ConjuntosElasticVaron,
    ConjuntosFranelaVaron,
    ConjuntosInterfilVaron,
    ConjuntosBosseVaron,
    ConjuntosNovaVaron,
    ConjuntosFranelaPlushVaron,
    ConjuntosPoliesterVaron,
    ConjuntosPolifreshVaron,
    ConjuntosTelaMojadaVaron,
    ConjuntosTerryVaron,
)
from .models import CNOConjuntoNovaNiño,CNOConjuntoInterfilNiño,CNAConjuntoNovaNiña,CNAConjuntoLicraNiña
from .models import (UVPantalonFranelaBotaRecta,UVPantalonNovaBotaRecta,UVPantalonTerryBotaRecta,UVPantalonInterfilBotaRecta,UVPantalonbossebotaRecta,UVPantaloncortavientobotaRecta,UVPantalonfranelabotajogger,UVPantalonterrybotajogger,UVPantalonetaslicravaron,UVcasacascortavientovaron,UVBividilicravaron,UVPpololicravaron,UVPpolocompresorvaron,UVPpoloalgodonvaron,UVshortterryvaron,UVshorttelamojadavaron,UVshortelasticvaron,UVshortnovavaron,UVpolooversizedama,UVpolooversizevaron)
from .models import UDpantalonpalazodama,UDpantalonnovabotarectadama,UDpantalonetalicradama,UDjoggercargodama,UDpantalonlomadama,UDpantaloninterfildama,UDpantalonfraneladama,UDpantalonlicrabotarectadama,UDpantalonterrydama,UDpantalonetaterrydama,UDjoggeroversizeterrydama,UDjoggerbotapiefraneladama,UDjoggerbotapieterrydama,UDjoggerinterfildama,UDjoggeroversizefraneladama,UDpololicramangalargadama,UDpololicramangacortadama,UDpolocroplicradama,UDsnikerlicradama,UDbikerlicradama,UDfaldashortdama,UDshortlicradama,UDshortterrydama,UDshorttelamojadadama,UDshortnovadama,UDpoloalgodonmangalargadama,UDpoloalgodocamiserodama,UDpoloalgodonmangacortadama,UDcasacalicradama,UDcasacacortavientodama,UDenterizodama,UDbivididama,UDtopdama
from .models import Cliente,Venta,Venta2
from django.utils import timezone
TEMPLATE_DIRS=('os.path.join(BASE_DIR, "templates")')

from .models import Ventas_Mensuale
from django.db.models import Sum
from collections import defaultdict
from django.utils.dateformat import DateFormat
from django.db.models.functions import TruncMonth

##############################################################################################
##############################################################################################
##############################################################################################



def listar_productos(request):
    filtro_tipo = request.GET.get('filtro', 'todos')
    filtro_color = request.GET.get('color', '')
    filtro_diseño = request.GET.get('diseño', '')
    filtro_codigo = request.GET.get('codigo', '')
    filtro_talla = request.GET.get('talla', '')
    filtro_marca = request.GET.get('marca', '')

##################################################################1111111111########################################################################################################################
    # Conjuntos Licra Dama
    if filtro_tipo == 'licra' or filtro_tipo == 'todos':
        licras = ConjuntosLicraDama.objects.all()
        if filtro_color:
            licras = licras.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            licras = licras.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            licras = licras.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            licras = licras.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            licras = licras.filter(Marca__icontains=filtro_marca)
    else:
        licras = ConjuntosLicraDama.objects.none()

##################################################################22222222222########################################################################################################################

    # Conjuntos Nova Dama
    if filtro_tipo == 'nova' or filtro_tipo == 'todos':
        novas = ConjuntosNovaDama.objects.all()
        if filtro_color:
            novas = novas.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            novas = novas.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            novas = novas.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            novas = novas.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            novas = novas.filter(Marca__icontains=filtro_marca)
    else:
        novas = ConjuntosNovaDama.objects.none()
##################################################################333333333333########################################################################################################################

    # Conjuntos Interfil Dama
    if filtro_tipo == 'interfil' or filtro_tipo == 'todos':
        interfiles = ConjuntosInterfilDama.objects.all()
        if filtro_color:
            interfiles = interfiles.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            interfiles = interfiles.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            interfiles = interfiles.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            interfiles = interfiles.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            interfiles = interfiles.filter(Marca__icontains=filtro_marca)
    else:
        interfiles = ConjuntosInterfilDama.objects.none()
##################################################################4444444444444444########################################################################################################################

    # Conjuntos Franela Dama
    if filtro_tipo == 'franela' or filtro_tipo == 'todos':
        franelas = ConjuntosFranelaDama.objects.all()
        if filtro_color:
            franelas = franelas.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            franelas = franelas.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            franelas = franelas.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            franelas = franelas.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            franelas = franelas.filter(Marca__icontains=filtro_marca)
    else:
        franelas = ConjuntosFranelaDama.objects.none()
    ##################################################################5555555555555555########################################################################################################################

    # Conjuntos Elastic Dama
    if filtro_tipo == 'elastic' or filtro_tipo == 'todos':
        elastics = ConjuntosElasticDama.objects.all()
        if filtro_color:
            elastics = elastics.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            elastics = elastics.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            elastics = elastics.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            elastics = elastics.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            elastics = elastics.filter(Marca__icontains=filtro_marca)
    else:
        elastics = ConjuntosElasticDama.objects.none()

##################################################################6666666666666########################################################################################################################

    # Conjuntos Plush Dama
    if filtro_tipo == 'plush' or filtro_tipo == 'todos':
        plushes = ConjuntosPlushDama.objects.all()
        if filtro_color:
            plushes = plushes.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            plushes = plushes.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            plushes = plushes.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            plushes = plushes.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            plushes = plushes.filter(Marca__icontains=filtro_marca)
    else:
        plushes = ConjuntosPlushDama.objects.none()
##################################################################77777777777777########################################################################################################################

    # Conjuntos Poliester Dama
    if filtro_tipo == 'poliester' or filtro_tipo == 'todos':
        poliesters = ConjuntosPoliesterDama.objects.all()
        if filtro_color:
            poliesters = poliesters.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poliesters = poliesters.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poliesters = poliesters.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poliesters = poliesters.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poliesters = poliesters.filter(Marca__icontains=filtro_marca)
    else:
        poliesters = ConjuntosPoliesterDama.objects.none()
##################################################################88888888888888888########################################################################################################################

    # Conjuntos Tela Mojada Dama
    if filtro_tipo == 'tela_mojada' or filtro_tipo == 'todos':
        telas_mojadas = ConjuntosTelaMojadaDama.objects.all()
        if filtro_color:
            telas_mojadas = telas_mojadas.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            telas_mojadas = telas_mojadas.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            telas_mojadas = telas_mojadas.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            telas_mojadas = telas_mojadas.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            telas_mojadas = telas_mojadas.filter(Marca__icontains=filtro_marca)
    else:
        telas_mojadas = ConjuntosTelaMojadaDama.objects.none()
##################################################################9999999999999999########################################################################################################################

    # Conjuntos Polifresh Dama
    if filtro_tipo == 'polifresh' or filtro_tipo == 'todos':
        polifreshes = ConjuntosPolifreshDama.objects.all()
        if filtro_color:
            polifreshes = polifreshes.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            polifreshes = polifreshes.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            polifreshes = polifreshes.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            polifreshes = polifreshes.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            polifreshes = polifreshes.filter(Marca__icontains=filtro_marca)
    else:
        polifreshes = ConjuntosPolifreshDama.objects.none()

##################################################################10 10 10 10 10 10########################################################################################################################
   # Conjuntos Loma Dama
    if filtro_tipo == 'loma' or filtro_tipo == 'todos':
        lomas = ConjuntosLomaDama.objects.all()
        if filtro_color:
            lomas = lomas.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            lomas = lomas.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            lomas = lomas.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            lomas = lomas.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            lomas = lomas.filter(Marca__icontains=filtro_marca)
    else:
        lomas = ConjuntosLomaDama.objects.none()


##################################################################11 11 11 11 11########################################################################################################################
    # Conjuntos Bosse Dama
    if filtro_tipo == 'bosse' or filtro_tipo == 'todos':
        bosses = ConjuntosBosseDama.objects.all()
        if filtro_color:
            bosses = bosses.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            bosses = bosses.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            bosses = bosses.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            bosses = bosses.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            bosses = bosses.filter(Marca__icontains=filtro_marca)
    else:
        bosses = ConjuntosBosseDama.objects.none()



##################################################################12 12 12 12 12########################################################################################################################

    # Conjuntos Terry Dama
    if filtro_tipo == 'terry' or filtro_tipo == 'todos':
        terrys = ConjuntosTerryDama.objects.all()
        if filtro_color:
            terrys = terrys.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            terrys = terrys.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            terrys = terrys.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            terrys = terrys.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            terrys = terrys.filter(Marca__icontains=filtro_marca)
    else:
        terrys = ConjuntosTerryDama.objects.none()


##################################################################13 13 13 13 13########################################################################################################################
    # Conjuntos Franela PLush Dama
    if filtro_tipo == 'franela_plush' or filtro_tipo == 'todos':
        franela_plushes = ConjuntosFranelaPLushDama.objects.all()
        if filtro_color:
            franela_plushes = franela_plushes.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            franela_plushes = franela_plushes.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            franela_plushes = franela_plushes.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            franela_plushes = franela_plushes.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            franela_plushes = franela_plushes.filter(Marca__icontains=filtro_marca)
    else:
        franela_plushes = ConjuntosFranelaPLushDama.objects.none()



##################################################################14 14 14 14 14########################################################################################################################
    # Conjuntos Cortaviento Reversible Dama
    if filtro_tipo == 'cortaviento_reversible' or filtro_tipo == 'todos':
        cortavientos_reversibles = ConjuntosCortavientoReversibleDama.objects.all()
        if filtro_color:
            cortavientos_reversibles = cortavientos_reversibles.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            cortavientos_reversibles = cortavientos_reversibles.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            cortavientos_reversibles = cortavientos_reversibles.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            cortavientos_reversibles = cortavientos_reversibles.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            cortavientos_reversibles = cortavientos_reversibles.filter(Marca__icontains=filtro_marca)
    else:
        cortavientos_reversibles = ConjuntosCortavientoReversibleDama.objects.none()


##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################

    # Conjuntos Cortaviento Reversible Varon
    if filtro_tipo == 'cortaviento_reversible_varon' or filtro_tipo == 'todos':
        cortavientos_reversibles_varones = ConjuntosCortavientoReversibleVaron.objects.all()
        if filtro_color:
            cortavientos_reversibles_varones = cortavientos_reversibles_varones.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            cortavientos_reversibles_varones = cortavientos_reversibles_varones.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            cortavientos_reversibles_varones = cortavientos_reversibles_varones.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            cortavientos_reversibles_varones = cortavientos_reversibles_varones.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            cortavientos_reversibles_varones = cortavientos_reversibles_varones.filter(Marca__icontains=filtro_marca)
    else:
        cortavientos_reversibles_varones = ConjuntosCortavientoReversibleVaron.objects.none()

##################################################################2222222 VARON########################################################################################################################
##################################################################2222222 VARON########################################################################################################################
##################################################################2222222 VARON########################################################################################################################
##################################################################2222222 VARON########################################################################################################################
    # Conjuntos Cortaviento  Varon
    if filtro_tipo == 'cortaviento_varon' or filtro_tipo == 'todos':
        cortavientos_varones = ConjuntosCortavientoVaron.objects.all()
        if filtro_color:
            cortavientos_varones = cortavientos_varones.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            cortavientos_varones = cortavientos_varones.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            cortavientos_varones = cortavientos_varones.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            cortavientos_varones = cortavientos_varones.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            cortavientos_varones = cortavientos_varones.filter(Marca__icontains=filtro_marca)
    else:
        cortavientos_varones = ConjuntosCortavientoVaron.objects.none()

#ConjuntosElasticVaron


##################################################################3333333 VARON########################################################################################################################
##################################################################3333333 VARON########################################################################################################################
##################################################################3333333 VARON########################################################################################################################
##################################################################3333333 VARON########################################################################################################################
    # Conjuntos elastic  Varon
    if filtro_tipo == 'elastic_varon' or filtro_tipo == 'todos':
        elastics_varon = ConjuntosElasticVaron.objects.all()
        if filtro_color:
            elastics_varon = elastics_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            elastics_varon = elastics_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            elastics_varon = elastics_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            elastics_varon = elastics_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            elastics_varon = elastics_varon.filter(Marca__icontains=filtro_marca)
    else:
        elastics_varon = ConjuntosElasticVaron.objects.none()

##################################################################4444444 VARON########################################################################################################################
##################################################################4444444 VARON########################################################################################################################
##################################################################4444444 VARON########################################################################################################################
##################################################################4444444 VARON########################################################################################################################
    # Conjuntos franela  Varon
    if filtro_tipo == 'franela_varon' or filtro_tipo == 'todos':
        franelas_varon = ConjuntosFranelaVaron.objects.all()
        if filtro_color:
            franelas_varon = franelas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            franelas_varon = franelas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            franelas_varon = franelas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            franelas_varon = franelas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            franelas_varon = franelas_varon.filter(Marca__icontains=filtro_marca)
    else:
        franelas_varon = ConjuntosFranelaVaron.objects.none()


##################################################################5555555 VARON########################################################################################################################
##################################################################5555555 VARON########################################################################################################################
##################################################################5555555 VARON########################################################################################################################
##################################################################5555555 VARON########################################################################################################################
    # Conjuntos interfill  Varon
    if filtro_tipo == 'interfil_varon' or filtro_tipo == 'todos':
        interfiles_varon = ConjuntosInterfilVaron.objects.all()
        if filtro_color:
            interfiles_varon = interfiles_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            interfiles_varon = interfiles_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            interfiles_varon = interfiles_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            interfiles_varon = interfiles_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            interfiles_varon = interfiles_varon.filter(Marca__icontains=filtro_marca)
    else:
        interfiles_varon = ConjuntosInterfilVaron.objects.none()

##################################################################6666666 VARON########################################################################################################################
##################################################################6666666 VARON########################################################################################################################
##################################################################6666666 VARON########################################################################################################################
##################################################################6666666 VARON########################################################################################################################
    # Conjuntos bosse  Varon
    if filtro_tipo == 'bosse_varon' or filtro_tipo == 'todos':
        bosses_varon = ConjuntosBosseVaron.objects.all()
        if filtro_color:
            bosses_varon = bosses_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            bosses_varon = bosses_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            bosses_varon = bosses_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            bosses_varon = bosses_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            bosses_varon = bosses_varon.filter(Marca__icontains=filtro_marca)
    else:
        bosses_varon = ConjuntosBosseVaron.objects.none()
##################################################################7777777 VARON########################################################################################################################
##################################################################7777777 VARON########################################################################################################################
##################################################################7777777 VARON########################################################################################################################
##################################################################7777777 VARON########################################################################################################################
    # Conjuntos nova  Varon
    if filtro_tipo == 'nova_varon' or filtro_tipo == 'todos':
        novas_varon = ConjuntosNovaVaron.objects.all()
        if filtro_color:
            novas_varon = novas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            novas_varon = novas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            novas_varon = novas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            novas_varon = novas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            novas_varon = novas_varon.filter(Marca__icontains=filtro_marca)
    else:
        novas_varon = ConjuntosNovaVaron.objects.none()
##################################################################8888888 VARON########################################################################################################################
##################################################################8888888 VARON########################################################################################################################
##################################################################8888888 VARON########################################################################################################################
##################################################################8888888 VARON########################################################################################################################
    # Conjuntos franela plush  Varon
    if filtro_tipo == 'franelaplush_varon' or filtro_tipo == 'todos':
        franelaplushes_varon = ConjuntosFranelaPlushVaron.objects.all()
        if filtro_color:
            franelaplushes_varon = franelaplushes_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            franelaplushes_varon = franelaplushes_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            franelaplushes_varon = franelaplushes_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            franelaplushes_varon = franelaplushes_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            franelaplushes_varon = franelaplushes_varon.filter(Marca__icontains=filtro_marca)
    else:
        franelaplushes_varon = ConjuntosFranelaPlushVaron.objects.none()

##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
    # Conjuntos franela poliester  Varon
    if filtro_tipo == 'poliester_varon' or filtro_tipo == 'todos':
        poliesters_varon = ConjuntosPoliesterVaron.objects.all()
        if filtro_color:
            poliesters_varon = poliesters_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poliesters_varon = poliesters_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poliesters_varon = poliesters_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poliesters_varon = poliesters_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poliesters_varon = poliesters_varon.filter(Marca__icontains=filtro_marca)
    else:
        poliesters_varon = ConjuntosPoliesterVaron.objects.none()
    

##################################################################10 10 10 10 VARON########################################################################################################################
##################################################################10 10 10 10 VARON########################################################################################################################
##################################################################10 10 10 10 VARON########################################################################################################################
##################################################################10 10 10 10 VARON########################################################################################################################
    # Conjuntos franela terry  Varon
    if filtro_tipo == 'terry_varon' or filtro_tipo == 'todos':
        terrys_varon = ConjuntosTerryVaron.objects.all()
        if filtro_color:
            terrys_varon = terrys_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            terrys_varon = terrys_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            terrys_varon = terrys_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            terrys_varon = terrys_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            terrys_varon = terrys_varon.filter(Marca__icontains=filtro_marca)
    else:
        terrys_varon = ConjuntosTerryVaron.objects.none()

##################################################################11 11 11 11 VARON########################################################################################################################
##################################################################11 11 11 11 VARON########################################################################################################################
##################################################################11 11 11 11 VARON########################################################################################################################
##################################################################11 11 11 11 VARON########################################################################################################################
    # Conjuntos franela terry  Varon
    if filtro_tipo == 'telamojada_varon' or filtro_tipo == 'todos':
        telamojadas_varon = ConjuntosTelaMojadaVaron.objects.all()
        if filtro_color:
            telamojadas_varon = telamojadas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            telamojadas_varon = telamojadas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            telamojadas_varon = telamojadas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            telamojadas_varon = telamojadas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            telamojadas_varon = telamojadas_varon.filter(Marca__icontains=filtro_marca)
    else:
        telamojadas_varon = ConjuntosTelaMojadaVaron.objects.none()

##################################################################12 12 12 12 VARON########################################################################################################################
##################################################################12 12 12 12 VARON########################################################################################################################
##################################################################12 12 12 12 VARON########################################################################################################################
##################################################################12 12 12 12 VARON########################################################################################################################
    # Conjuntos  polifresh  Varon
    if filtro_tipo == 'polifresh_varon' or filtro_tipo == 'todos':
        polifreshes_varon = ConjuntosPolifreshVaron.objects.all()
        if filtro_color:
            polifreshes_varon = polifreshes_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            polifreshes_varon = polifreshes_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            polifreshes_varon = polifreshes_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            polifreshes_varon = polifreshes_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            polifreshes_varon = polifreshes_varon.filter(Marca__icontains=filtro_marca)
    else:
        polifreshes_varon = ConjuntosPolifreshVaron.objects.none()






##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################
    # PANTALON FRANELA BOTA RECTA VARON
    if filtro_tipo == 'pantalonfranelabotarecta_varon' or filtro_tipo == 'todos':
        pantalonfranelabotarectas_varon = UVPantalonFranelaBotaRecta.objects.all()
        if filtro_color:
            pantalonfranelabotarectas_varon = pantalonfranelabotarectas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonfranelabotarectas_varon = pantalonfranelabotarectas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonfranelabotarectas_varon = pantalonfranelabotarectas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonfranelabotarectas_varon = pantalonfranelabotarectas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonfranelabotarectas_varon = pantalonfranelabotarectas_varon.filter(Marca__icontains=filtro_marca)
    else:
        pantalonfranelabotarectas_varon = UVPantalonFranelaBotaRecta.objects.none()




##################################################################2222222 VARON########################################################################################################################
##################################################################2222222 VARON########################################################################################################################
##################################################################2222222 VARON########################################################################################################################
##################################################################2222222 VARON########################################################################################################################
    # PANTALON FRANELA BOTA RECTA VARON
    if filtro_tipo == 'pantalonnovabotarecta_varon' or filtro_tipo == 'todos':
        pantalonnovabotarectas_varon = UVPantalonNovaBotaRecta.objects.all()
        if filtro_color:
            pantalonnovabotarectas_varon = pantalonnovabotarectas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonnovabotarectas_varon = pantalonnovabotarectas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonnovabotarectas_varon = pantalonnovabotarectas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonnovabotarectas_varon = pantalonnovabotarectas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonnovabotarectas_varon = pantalonnovabotarectas_varon.filter(Marca__icontains=filtro_marca)
    else:
        pantalonnovabotarectas_varon = UVPantalonNovaBotaRecta.objects.none()

##################################################################3333333 VARON########################################################################################################################
##################################################################3333333 VARON########################################################################################################################
##################################################################3333333 VARON########################################################################################################################
##################################################################3333333 VARON########################################################################################################################
    # PANTALON FRANELA BOTA RECTA VARON
    if filtro_tipo == 'pantalonterrybotarecta_varon' or filtro_tipo == 'todos':
        pantalonterrybotarectas_varon = UVPantalonTerryBotaRecta.objects.all()
        if filtro_color:
            pantalonterrybotarectas_varon = pantalonterrybotarectas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonterrybotarectas_varon = pantalonterrybotarectas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonterrybotarectas_varon = pantalonterrybotarectas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonterrybotarectas_varon = pantalonterrybotarectas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonterrybotarectas_varon = pantalonterrybotarectas_varon.filter(Marca__icontains=filtro_marca)
    else:
        pantalonterrybotarectas_varon = UVPantalonTerryBotaRecta.objects.none()

##################################################################4444444 VARON########################################################################################################################
##################################################################4444444 VARON########################################################################################################################
##################################################################4444444 VARON########################################################################################################################
##################################################################4444444 VARON########################################################################################################################
    # PANTALON FRANELA BOTA RECTA VARON
    if filtro_tipo == 'pantaloninterfilbotarecta_varon' or filtro_tipo == 'todos':
        pantaloninterfilbotarectas_varon = UVPantalonInterfilBotaRecta.objects.all()
        if filtro_color:
            pantaloninterfilbotarectas_varon = pantaloninterfilbotarectas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantaloninterfilbotarectas_varon = pantaloninterfilbotarectas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantaloninterfilbotarectas_varon = pantaloninterfilbotarectas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantaloninterfilbotarectas_varon = pantaloninterfilbotarectas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantaloninterfilbotarectas_varon = pantaloninterfilbotarectas_varon.filter(Marca__icontains=filtro_marca)
    else:
        pantaloninterfilbotarectas_varon = UVPantalonInterfilBotaRecta.objects.none()



##################################################################5555555 VARON########################################################################################################################
##################################################################5555555 VARON########################################################################################################################
##################################################################5555555 VARON########################################################################################################################
##################################################################5555555 VARON########################################################################################################################
    # PANTALON FRANELA BOTA RECTA VARON
    if filtro_tipo == 'pantalonbossebotarecta_varon' or filtro_tipo == 'todos':
        pantalonbossebotarectas_varon = UVPantalonbossebotaRecta.objects.all()
        if filtro_color:
            pantalonbossebotarectas_varon = pantalonbossebotarectas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonbossebotarectas_varon = pantalonbossebotarectas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonbossebotarectas_varon = pantalonbossebotarectas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonbossebotarectas_varon = pantalonbossebotarectas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonbossebotarectas_varon = pantalonbossebotarectas_varon.filter(Marca__icontains=filtro_marca)
    else:
        pantalonbossebotarectas_varon = UVPantalonbossebotaRecta.objects.none()


##################################################################6666666 VARON########################################################################################################################
##################################################################6666666 VARON########################################################################################################################
##################################################################6666666 VARON########################################################################################################################
##################################################################6666666 VARON########################################################################################################################
    # PANTALON FRANELA BOTA RECTA VARON
    if filtro_tipo == 'pantaloncortavientobotarecta_varon' or filtro_tipo == 'todos':
        pantaloncortavientobotarectas_varon = UVPantaloncortavientobotaRecta.objects.all()
        if filtro_color:
            pantaloncortavientobotarectas_varon = pantaloncortavientobotarectas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantaloncortavientobotarectas_varon = pantaloncortavientobotarectas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantaloncortavientobotarectas_varon = pantaloncortavientobotarectas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantaloncortavientobotarectas_varon = pantaloncortavientobotarectas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantaloncortavientobotarectas_varon = pantaloncortavientobotarectas_varon.filter(Marca__icontains=filtro_marca)
    else:
        pantaloncortavientobotarectas_varon = UVPantaloncortavientobotaRecta.objects.none()

##################################################################7777777 VARON########################################################################################################################
##################################################################7777777 VARON########################################################################################################################
##################################################################7777777 VARON########################################################################################################################
##################################################################7777777 VARON########################################################################################################################
    # PANTALON FRANELA BOTA RECTA VARON
    if filtro_tipo == 'joggerfranela_varon' or filtro_tipo == 'todos':
        joggerfranelas_varon = UVPantalonfranelabotajogger.objects.all()
        if filtro_color:
            joggerfranelas_varon = joggerfranelas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggerfranelas_varon = joggerfranelas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggerfranelas_varon = joggerfranelas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggerfranelas_varon = joggerfranelas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggerfranelas_varon = joggerfranelas_varon.filter(Marca__icontains=filtro_marca)
    else:
        joggerfranelas_varon = UVPantalonfranelabotajogger.objects.none()

##################################################################8888888 VARON########################################################################################################################
##################################################################8888888 VARON########################################################################################################################
##################################################################8888888 VARON########################################################################################################################
##################################################################8888888 VARON########################################################################################################################
    if filtro_tipo == 'joggerterry_varon' or filtro_tipo == 'todos':
        joggerterrys_varon = UVPantalonterrybotajogger.objects.all()
        if filtro_color:
            joggerterrys_varon = joggerterrys_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggerterrys_varon = joggerterrys_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggerterrys_varon = joggerterrys_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggerterrys_varon = joggerterrys_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggerterrys_varon = joggerterrys_varon.filter(Marca__icontains=filtro_marca)
    else:
        joggerterrys_varon = UVPantalonterrybotajogger.objects.none()

#UVPantalonetaslicravaron,UVcasacascortavientovaron,UVBividilicravaron)

##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
    if filtro_tipo == 'pantalonetalicra_varon' or filtro_tipo == 'todos':
        pantalonetalicras_varon = UVPantalonetaslicravaron.objects.all()
        if filtro_color:
            pantalonetalicras_varon = pantalonetalicras_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonetalicras_varon = pantalonetalicras_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonetalicras_varon = pantalonetalicras_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonetalicras_varon = pantalonetalicras_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonetalicras_varon = pantalonetalicras_varon.filter(Marca__icontains=filtro_marca)
    else:
        pantalonetalicras_varon = UVPantalonetaslicravaron.objects.none()
##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
##################################################################9999999 VARON########################################################################################################################
    if filtro_tipo == 'casacacortaviento_varon' or filtro_tipo == 'todos':
        casacascortavientos_varon = UVcasacascortavientovaron.objects.all()
        if filtro_color:
            casacascortavientos_varon = casacascortavientos_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            casacascortavientos_varon = casacascortavientos_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            casacascortavientos_varon = casacascortavientos_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            casacascortavientos_varon = casacascortavientos_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            casacascortavientos_varon = casacascortavientos_varon.filter(Marca__icontains=filtro_marca)
    else:
        casacascortavientos_varon = UVcasacascortavientovaron.objects.none()
##################################################################1010101 VARON########################################################################################################################
##################################################################1010101 VARON########################################################################################################################
##################################################################1010101 VARON########################################################################################################################
##################################################################1010101 VARON########################################################################################################################
    if filtro_tipo == 'bividilicra_varon' or filtro_tipo == 'todos':
        bividislicras_varon = UVBividilicravaron.objects.all()
        if filtro_color:
            bividislicras_varon = bividislicras_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            bividislicras_varon = bividislicras_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            bividislicras_varon = bividislicras_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            bividislicras_varon = bividislicras_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            bividislicras_varon = bividislicras_varon.filter(Marca__icontains=filtro_marca)
    else:
        bividislicras_varon = UVBividilicravaron.objects.none()
##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################
##################################################################1111111 VARON########################################################################################################################

#,UVPpolocompresorvaron,)

    if filtro_tipo == 'pololicra_varon' or filtro_tipo == 'todos':
        poloslicras_varon = UVPpololicravaron.objects.all()
        if filtro_color:
            poloslicras_varon = poloslicras_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloslicras_varon = poloslicras_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloslicras_varon = poloslicras_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloslicras_varon = poloslicras_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloslicras_varon = poloslicras_varon.filter(Marca__icontains=filtro_marca)
    else:
        poloslicras_varon = UVPpololicravaron.objects.none()

##################################################################1212121 VARON########################################################################################################################
##################################################################1212121 VARON########################################################################################################################
##################################################################1212121 VARON########################################################################################################################
##################################################################1212121 VARON########################################################################################################################

    if filtro_tipo == 'poloalgodon_varon' or filtro_tipo == 'todos':
        polosalgodones_varon = UVPpoloalgodonvaron.objects.all()
        if filtro_color:
            polosalgodones_varon = polosalgodones_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            polosalgodones_varon = polosalgodones_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            polosalgodones_varon = polosalgodones_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            polosalgodones_varon = polosalgodones_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            polosalgodones_varon = polosalgodones_varon.filter(Marca__icontains=filtro_marca)
    else:
        polosalgodones_varon = UVPpoloalgodonvaron.objects.none()

##################################################################1313131 VARON########################################################################################################################
##################################################################1313131 VARON########################################################################################################################
##################################################################1313131 VARON########################################################################################################################
##################################################################1313131 VARON########################################################################################################################

    if filtro_tipo == 'polocompresor_varon' or filtro_tipo == 'todos':
        poloscompresor_varon = UVPpolocompresorvaron.objects.all()
        if filtro_color:
            poloscompresor_varon = poloscompresor_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloscompresor_varon = poloscompresor_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloscompresor_varon = poloscompresor_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloscompresor_varon = poloscompresor_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloscompresor_varon = poloscompresor_varon.filter(Marca__icontains=filtro_marca)
    else:
        poloscompresor_varon = UVPpolocompresorvaron.objects.none()


##################################################################1414141 VARON########################################################################################################################
##################################################################1414141 VARON########################################################################################################################
##################################################################1414141 VARON########################################################################################################################
##################################################################1414141 VARON########################################################################################################################
    if filtro_tipo == 'shortterry_varon' or filtro_tipo == 'todos':
        shortterrys_varon = UVshortterryvaron.objects.all()
        if filtro_color:
            shortterrys_varon = shortterrys_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shortterrys_varon = shortterrys_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shortterrys_varon = shortterrys_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shortterrys_varon = shortterrys_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shortterrys_varon = shortterrys_varon.filter(Marca__icontains=filtro_marca)
    else:
        shortterrys_varon = UVshortterryvaron.objects.none()


##################################################################1515151 VARON########################################################################################################################
##################################################################1515151 VARON########################################################################################################################
##################################################################1515151 VARON########################################################################################################################
##################################################################1515151 VARON########################################################################################################################
    if filtro_tipo == 'shorttelamojada_varon' or filtro_tipo == 'todos':
        shorttelamojadas_varon = UVshorttelamojadavaron.objects.all()
        if filtro_color:
            shorttelamojadas_varon = shorttelamojadas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shorttelamojadas_varon = shorttelamojadas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shorttelamojadas_varon = shorttelamojadas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shorttelamojadas_varon = shorttelamojadas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shorttelamojadas_varon = shorttelamojadas_varon.filter(Marca__icontains=filtro_marca)
    else:
        shorttelamojadas_varon = UVshorttelamojadavaron.objects.none()


##################################################################1616161 VARON########################################################################################################################
##################################################################1616161 VARON########################################################################################################################
##################################################################1616161 VARON########################################################################################################################
##################################################################1616161 VARON########################################################################################################################
    if filtro_tipo == 'shortelastic_varon' or filtro_tipo == 'todos':
        shortelastics_varon = UVshortelasticvaron.objects.all()
        if filtro_color:
            shortelastics_varon = shortelastics_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shortelastics_varon = shortelastics_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shortelastics_varon = shortelastics_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shortelastics_varon = shortelastics_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shortelastics_varon = shortelastics_varon.filter(Marca__icontains=filtro_marca)
    else:
        shortelastics_varon = UVshortelasticvaron.objects.none()


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'shortnova_varon' or filtro_tipo == 'todos':
        shortnovas_varon = UVshortnovavaron.objects.all()
        if filtro_color:
            shortnovas_varon = shortnovas_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shortnovas_varon = shortnovas_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shortnovas_varon = shortnovas_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shortnovas_varon = shortnovas_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shortnovas_varon = shortnovas_varon.filter(Marca__icontains=filtro_marca)
    else:
        shortnovas_varon = UVshortnovavaron.objects.none()

#,


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################


    if filtro_tipo == 'pantalonetalicra_dama' or filtro_tipo == 'todos':
        pantalonetaslicra_dama = UDpantalonetalicradama.objects.all()
        if filtro_color:
            pantalonetaslicra_dama = pantalonetaslicra_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonetaslicra_dama = pantalonetaslicra_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonetaslicra_dama = pantalonetaslicra_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonetaslicra_dama = pantalonetaslicra_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonetaslicra_dama = pantalonetaslicra_dama.filter(Marca__icontains=filtro_marca)

    else:
        pantalonetaslicra_dama = UDpantalonetalicradama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantalonbotarectanova_dama' or filtro_tipo == 'todos':
        pantalonesbotarectanova_dama = UDpantalonnovabotarectadama.objects.all()
        if filtro_color:
            pantalonesbotarectanova_dama = pantalonesbotarectanova_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonesbotarectanova_dama = pantalonesbotarectanova_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonesbotarectanova_dama = pantalonesbotarectanova_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonesbotarectanova_dama = pantalonesbotarectanova_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonesbotarectanova_dama = pantalonesbotarectanova_dama.filter(Marca__icontains=filtro_marca)
    else:
        pantalonesbotarectanova_dama = UDpantalonnovabotarectadama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'joggercargo_dama' or filtro_tipo == 'todos':
        joggercargos_dama = UDjoggercargodama.objects.all()
        if filtro_color:
            joggercargos_dama = joggercargos_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggercargos_dama = joggercargos_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggercargos_dama = joggercargos_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggercargos_dama = joggercargos_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggercargos_dama = joggercargos_dama.filter(Marca__icontains=filtro_marca)
    else:
        joggercargos_dama = UDjoggercargodama.objects.none()



#,,,,UDpantalonterrydama
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantalonloma_dama' or filtro_tipo == 'todos':
        pantalonlomas_dama = UDpantalonlomadama.objects.all()
        if filtro_color:
            pantalonlomas_dama = pantalonlomas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonlomas_dama = pantalonlomas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonlomas_dama = pantalonlomas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonlomas_dama = pantalonlomas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonlomas_dama = pantalonlomas_dama.filter(Marca__icontains=filtro_marca)
    else:
        pantalonlomas_dama = UDpantalonlomadama.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantaloninterfil_dama' or filtro_tipo == 'todos':
        pantaloninterfils_dama = UDpantaloninterfildama.objects.all()
        if filtro_color:
            pantaloninterfils_dama = pantaloninterfils_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantaloninterfils_dama = pantaloninterfils_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantaloninterfils_dama = pantaloninterfils_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantaloninterfils_dama = pantaloninterfils_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantaloninterfils_dama = pantaloninterfils_dama.filter(Marca__icontains=filtro_marca)
    else:
        pantaloninterfils_dama = UDpantaloninterfildama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantalonfranela_dama' or filtro_tipo == 'todos':
        pantalonfranelas_dama = UDpantalonfraneladama.objects.all()
        if filtro_color:
            pantalonfranelas_dama = pantalonfranelas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonfranelas_dama = pantalonfranelas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonfranelas_dama = pantalonfranelas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonfranelas_dama = pantalonfranelas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonfranelas_dama = pantalonfranelas_dama.filter(Marca__icontains=filtro_marca)
    else:
        pantalonfranelas_dama = UDpantalonfraneladama.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantalonlicrabotarecta_dama' or filtro_tipo == 'todos':
        pantalonlicrabotarectas_dama = UDpantalonlicrabotarectadama.objects.all()
        if filtro_color:
            pantalonlicrabotarectas_dama = pantalonlicrabotarectas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonlicrabotarectas_dama = pantalonlicrabotarectas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonlicrabotarectas_dama = pantalonlicrabotarectas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonlicrabotarectas_dama = pantalonlicrabotarectas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonlicrabotarectas_dama = pantalonlicrabotarectas_dama.filter(Marca__icontains=filtro_marca)
    else:
        pantalonlicrabotarectas_dama = UDpantalonlicrabotarectadama.objects.none()


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantalonterry_dama' or filtro_tipo == 'todos':
        pantalonterrys_dama = UDpantalonterrydama.objects.all()
        if filtro_color:
            pantalonterrys_dama = pantalonterrys_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonterrys_dama = pantalonterrys_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonterrys_dama = pantalonterrys_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonterrys_dama = pantalonterrys_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonterrys_dama = pantalonterrys_dama.filter(Marca__icontains=filtro_marca)
    else:
        pantalonterrys_dama = UDpantalonterrydama.objects.none()
        
#

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantalonetaterry_dama' or filtro_tipo == 'todos':
        pantalonetaterrys_dama = UDpantalonetaterrydama.objects.all()
        if filtro_color:
            pantalonetaterrys_dama = pantalonetaterrys_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonetaterrys_dama = pantalonetaterrys_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonetaterrys_dama = pantalonetaterrys_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonetaterrys_dama = pantalonetaterrys_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonetaterrys_dama = pantalonetaterrys_dama.filter(Marca__icontains=filtro_marca)
    else:
        pantalonetaterrys_dama = UDpantalonetaterrydama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'joggeroversizeterry_dama' or filtro_tipo == 'todos':
        joggeroversizeterrys_dama = UDjoggeroversizeterrydama.objects.all()
        if filtro_color:
            joggeroversizeterrys_dama = joggeroversizeterrys_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggeroversizeterrys_dama = joggeroversizeterrys_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggeroversizeterrys_dama = joggeroversizeterrys_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggeroversizeterrys_dama = joggeroversizeterrys_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggeroversizeterrys_dama = joggeroversizeterrys_dama.filter(Marca__icontains=filtro_marca)
    else:
        joggeroversizeterrys_dama = UDjoggeroversizeterrydama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'joggeroversizefranela_dama' or filtro_tipo == 'todos':
        joggeroversizefranelas_dama = UDjoggeroversizefraneladama.objects.all()
        if filtro_color:
            joggeroversizefranelas_dama = joggeroversizefranelas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggeroversizefranelas_dama = joggeroversizefranelas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggeroversizefranelas_dama = joggeroversizefranelas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggeroversizefranelas_dama = joggeroversizefranelas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggeroversizefranelas_dama = joggeroversizefranelas_dama.filter(Marca__icontains=filtro_marca)
    else:
        joggeroversizefranelas_dama = UDjoggeroversizefraneladama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'joggerbotapieterry_dama' or filtro_tipo == 'todos':
        joggerbotapieterrys_dama = UDjoggerbotapieterrydama.objects.all()
        if filtro_color:
            joggerbotapieterrys_dama = joggerbotapieterrys_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggerbotapieterrys_dama = joggerbotapieterrys_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggerbotapieterrys_dama = joggerbotapieterrys_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggerbotapieterrys_dama = joggerbotapieterrys_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggerbotapieterrys_dama = joggerbotapieterrys_dama.filter(Marca__icontains=filtro_marca)
    else:
        joggerbotapieterrys_dama = UDjoggerbotapieterrydama.objects.none()


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pantalonpalazo_dama' or filtro_tipo == 'todos':
        pantalonpalazosdama = UDpantalonpalazodama.objects.all()
        if filtro_color:
            pantalonpalazosdama = pantalonpalazosdama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pantalonpalazosdama = pantalonpalazosdama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pantalonpalazosdama = pantalonpalazosdama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pantalonpalazosdama = pantalonpalazosdama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pantalonpalazosdama = pantalonpalazosdama.filter(Marca__icontains=filtro_marca)
    else:
        pantalonpalazosdama = UDpantalonpalazodama.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'joggerbotapiefranela_dama' or filtro_tipo == 'todos':
        joggerbotapiefranelas_dama = UDjoggerbotapiefraneladama.objects.all()
        if filtro_color:
            joggerbotapiefranelas_dama = joggerbotapiefranelas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggerbotapiefranelas_dama = joggerbotapiefranelas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggerbotapiefranelas_dama = joggerbotapiefranelas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggerbotapiefranelas_dama = joggerbotapiefranelas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggerbotapiefranelas_dama = joggerbotapiefranelas_dama.filter(Marca__icontains=filtro_marca)
    else:
        joggerbotapiefranelas_dama = UDjoggerbotapiefraneladama.objects.none()

#UDjoggerinterfildama


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'joggerinterfil_dama' or filtro_tipo == 'todos':
        joggerinterfils_dama = UDjoggerinterfildama.objects.all()
        if filtro_color:
            joggerinterfils_dama = joggerinterfils_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            joggerinterfils_dama = joggerinterfils_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            joggerinterfils_dama = joggerinterfils_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            joggerinterfils_dama = joggerinterfils_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            joggerinterfils_dama = joggerinterfils_dama.filter(Marca__icontains=filtro_marca)
    else:
        joggerinterfils_dama = UDjoggerinterfildama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pololicramangalarga_dama' or filtro_tipo == 'todos':
        poloslicramangalarga_dama = UDpololicramangalargadama.objects.all()
        if filtro_color:
            poloslicramangalarga_dama = poloslicramangalarga_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloslicramangalarga_dama = poloslicramangalarga_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloslicramangalarga_dama = poloslicramangalarga_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloslicramangalarga_dama = poloslicramangalarga_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloslicramangalarga_dama = poloslicramangalarga_dama.filter(Marca__icontains=filtro_marca)
    else:
        poloslicramangalarga_dama = UDpololicramangalargadama.objects.none()


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'pololicramangacorta_dama' or filtro_tipo == 'todos':
        pololicrasmangacorta_dama = UDpololicramangacortadama.objects.all()
        if filtro_color:
            pololicrasmangacorta_dama = pololicrasmangacorta_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            pololicrasmangacorta_dama = pololicrasmangacorta_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            pololicrasmangacorta_dama = pololicrasmangacorta_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            pololicrasmangacorta_dama = pololicrasmangacorta_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            pololicrasmangacorta_dama = pololicrasmangacorta_dama.filter(Marca__icontains=filtro_marca)
    else:
        pololicrasmangacorta_dama = UDpololicramangacortadama.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'polocroplicra_dama' or filtro_tipo == 'todos':
        poloscroplicra_dama = UDpolocroplicradama.objects.all()
        if filtro_color:
            poloscroplicra_dama = poloscroplicra_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloscroplicra_dama = poloscroplicra_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloscroplicra_dama = poloscroplicra_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloscroplicra_dama = poloscroplicra_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloscroplicra_dama = poloscroplicra_dama.filter(Marca__icontains=filtro_marca)
    else:
        poloscroplicra_dama = UDpolocroplicradama.objects.none()


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'snikerlicra_dama' or filtro_tipo == 'todos':
        snikerslicra_dama = UDsnikerlicradama.objects.all()
        if filtro_color:
            snikerslicra_dama = snikerslicra_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            snikerslicra_dama = snikerslicra_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            snikerslicra_dama = snikerslicra_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            snikerslicra_dama = snikerslicra_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            snikerslicra_dama = snikerslicra_dama.filter(Marca__icontains=filtro_marca)
    else:
        snikerslicra_dama = UDsnikerlicradama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'bikerlicra_dama' or filtro_tipo == 'todos':
        bikerslicra_dama = UDbikerlicradama.objects.all()
        if filtro_color:
            bikerslicra_dama = bikerslicra_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            bikerslicra_dama = bikerslicra_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            bikerslicra_dama = bikerslicra_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            bikerslicra_dama = bikerslicra_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            bikerslicra_dama = bikerslicra_dama.filter(Marca__icontains=filtro_marca)
    else:
        bikerslicra_dama = UDbikerlicradama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'faldashortlicra_dama' or filtro_tipo == 'todos':
        faldashortslicra_dama = UDfaldashortdama.objects.all()
        if filtro_color:
            faldashortslicra_dama = faldashortslicra_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            faldashortslicra_dama = faldashortslicra_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            faldashortslicra_dama = faldashortslicra_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            faldashortslicra_dama = faldashortslicra_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            faldashortslicra_dama = faldashortslicra_dama.filter(Marca__icontains=filtro_marca)
    else:
        faldashortslicra_dama = UDfaldashortdama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'shortlicra_dama' or filtro_tipo == 'todos':
        shortslicra_dama = UDshortlicradama.objects.all()
        if filtro_color:
            shortslicra_dama = shortslicra_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shortslicra_dama = shortslicra_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shortslicra_dama = shortslicra_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shortslicra_dama = shortslicra_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shortslicra_dama = shortslicra_dama.filter(Marca__icontains=filtro_marca)
    else:
        shortslicra_dama = UDshortlicradama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'shortterry_dama' or filtro_tipo == 'todos':
        shortterrys_dama = UDshortterrydama.objects.all()
        if filtro_color:
            shortterrys_dama = shortterrys_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shortterrys_dama = shortterrys_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shortterrys_dama = shortterrys_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shortterrys_dama = shortterrys_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shortterrys_dama = shortterrys_dama.filter(Marca__icontains=filtro_marca)
    else:
        shortterrys_dama = UDshortterrydama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'shorttelamojada_dama' or filtro_tipo == 'todos':
        shorttelamojadas_dama = UDshorttelamojadadama.objects.all()
        if filtro_color:
            shorttelamojadas_dama = shorttelamojadas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shorttelamojadas_dama = shorttelamojadas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shorttelamojadas_dama = shorttelamojadas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shorttelamojadas_dama = shorttelamojadas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shorttelamojadas_dama = shorttelamojadas_dama.filter(Marca__icontains=filtro_marca)
    else:
        shorttelamojadas_dama = UDshorttelamojadadama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'shortnovadama' or filtro_tipo == 'todos':
        shortnovasdama = UDshortnovadama.objects.all()
        if filtro_color:
            shortnovasdama = shortnovasdama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            shortnovasdama = shortnovasdama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            shortnovasdama = shortnovasdama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            shortnovasdama = shortnovasdama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            shortnovasdama = shortnovasdama.filter(Marca__icontains=filtro_marca)
    else:
        shortnovasdama = UDshortnovadama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'poloalgodonmangalarga_dama' or filtro_tipo == 'todos':
        poloalgodonmangalargas_dama = UDpoloalgodonmangalargadama.objects.all()
        if filtro_color:
            poloalgodonmangalargas_dama = poloalgodonmangalargas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloalgodonmangalargas_dama = poloalgodonmangalargas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloalgodonmangalargas_dama = poloalgodonmangalargas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloalgodonmangalargas_dama = poloalgodonmangalargas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloalgodonmangalargas_dama = poloalgodonmangalargas_dama.filter(Marca__icontains=filtro_marca)
    else:
        poloalgodonmangalargas_dama = UDpoloalgodonmangalargadama.objects.none()


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'poloalgodonmangacorta_dama' or filtro_tipo == 'todos':
        poloalgodonmangacortas_dama = UDpoloalgodonmangacortadama.objects.all()
        if filtro_color:
            poloalgodonmangacortas_dama = poloalgodonmangacortas_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloalgodonmangacortas_dama = poloalgodonmangacortas_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloalgodonmangacortas_dama = poloalgodonmangacortas_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloalgodonmangacortas_dama = poloalgodonmangacortas_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloalgodonmangacortas_dama = poloalgodonmangacortas_dama.filter(Marca__icontains=filtro_marca)
    else:
        poloalgodonmangacortas_dama = UDpoloalgodonmangacortadama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'polocuellocamisero_dama' or filtro_tipo == 'todos':
        polocuellocamiseros_dama = UDpoloalgodocamiserodama.objects.all()
        if filtro_color:
            polocuellocamiseros_dama = polocuellocamiseros_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            polocuellocamiseros_dama = polocuellocamiseros_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            polocuellocamiseros_dama = polocuellocamiseros_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            polocuellocamiseros_dama = polocuellocamiseros_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            polocuellocamiseros_dama = polocuellocamiseros_dama.filter(Marca__icontains=filtro_marca)
    else:
        polocuellocamiseros_dama = UDpoloalgodocamiserodama.objects.none()


#,

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'casacalicra_dama' or filtro_tipo == 'todos':
        casacalicras_dama = UDcasacalicradama.objects.all()
        if filtro_color:
            casacalicras_dama = casacalicras_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            casacalicras_dama = casacalicras_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            casacalicras_dama = casacalicras_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            casacalicras_dama = casacalicras_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            casacalicras_dama = casacalicras_dama.filter(Marca__icontains=filtro_marca)
    else:
        casacalicras_dama = UDcasacalicradama.objects.none()


##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'casacacortaviento_dama' or filtro_tipo == 'todos':
        casacacortavientos_dama = UDcasacacortavientodama.objects.all()
        if filtro_color:
            casacacortavientos_dama = casacacortavientos_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            casacacortavientos_dama = casacacortavientos_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            casacacortavientos_dama = casacacortavientos_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            casacacortavientos_dama = casacacortavientos_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            casacacortavientos_dama = casacacortavientos_dama.filter(Marca__icontains=filtro_marca)
    else:
        casacacortavientos_dama = UDcasacacortavientodama.objects.none()

#UDenterizodama,UDbivididama,UDtopdama
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'enterizo_dama' or filtro_tipo == 'todos':
        enterizos_dama = UDenterizodama.objects.all()
        if filtro_color:
            enterizos_dama = enterizos_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            enterizos_dama = enterizos_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            enterizos_dama = enterizos_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            enterizos_dama = enterizos_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            enterizos_dama = enterizos_dama.filter(Marca__icontains=filtro_marca)
    else:
        enterizos_dama = UDenterizodama.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'bividi_dama' or filtro_tipo == 'todos':
        bividis_dama = UDbivididama.objects.all()
        if filtro_color:
            bividis_dama = bividis_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            bividis_dama = bividis_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            bividis_dama = bividis_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            bividis_dama = bividis_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            bividis_dama = bividis_dama.filter(Marca__icontains=filtro_marca)
    else:
        bividis_dama = UDbivididama.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'top_dama' or filtro_tipo == 'todos':
        tops_dama = UDtopdama.objects.all()
        if filtro_color:
            tops_dama = tops_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            tops_dama = tops_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            tops_dama = tops_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            tops_dama = tops_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            tops_dama = tops_dama.filter(Marca__icontains=filtro_marca)
    else:
        tops_dama = UDtopdama.objects.none()

#from .models import ,,CNAConjuntoNovaNiña,CNAConjuntoLicraNiña
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'ConjuntoNova_Niño' or filtro_tipo == 'todos':
        ConjuntoNovas_Niño = CNOConjuntoNovaNiño.objects.all()
        if filtro_color:
            ConjuntoNovas_Niño = ConjuntoNovas_Niño.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            ConjuntoNovas_Niño = ConjuntoNovas_Niño.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            ConjuntoNovas_Niño = ConjuntoNovas_Niño.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            ConjuntoNovas_Niño = ConjuntoNovas_Niño.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            ConjuntoNovas_Niño = ConjuntoNovas_Niño.filter(Marca__icontains=filtro_marca)
    else:
        ConjuntoNovas_Niño = CNOConjuntoNovaNiño.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'ConjuntoInterfil_Niño' or filtro_tipo == 'todos':
        ConjuntoInterfils_Niño = CNOConjuntoInterfilNiño.objects.all()
        if filtro_color:
            ConjuntoInterfils_Niño = ConjuntoInterfils_Niño.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            ConjuntoInterfils_Niño = ConjuntoInterfils_Niño.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            ConjuntoInterfils_Niño = ConjuntoInterfils_Niño.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            ConjuntoInterfils_Niño = ConjuntoInterfils_Niño.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            ConjuntoInterfils_Niño = ConjuntoInterfils_Niño.filter(Marca__icontains=filtro_marca)
    else:
        ConjuntoInterfils_Niño = CNOConjuntoInterfilNiño.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'ConjuntoNova_Niña' or filtro_tipo == 'todos':
        ConjuntoNovas_Niña = CNAConjuntoNovaNiña.objects.all()
        if filtro_color:
            ConjuntoNovas_Niña = ConjuntoNovas_Niña.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            ConjuntoNovas_Niña = ConjuntoNovas_Niña.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            ConjuntoNovas_Niña = ConjuntoNovas_Niña.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            ConjuntoNovas_Niña = ConjuntoNovas_Niña.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            ConjuntoNovas_Niña = ConjuntoNovas_Niña.filter(Marca__icontains=filtro_marca)
    else:
        ConjuntoNovas_Niña = CNAConjuntoNovaNiña.objects.none()

##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'ConjuntoLicra_Niña' or filtro_tipo == 'todos':
        ConjuntoLicras_Niña = CNAConjuntoLicraNiña.objects.all()
        if filtro_color:
            ConjuntoLicras_Niña = ConjuntoLicras_Niña.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            ConjuntoLicras_Niña = ConjuntoLicras_Niña.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            ConjuntoLicras_Niña = ConjuntoLicras_Niña.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            ConjuntoLicras_Niña = ConjuntoLicras_Niña.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            ConjuntoLicras_Niña = ConjuntoLicras_Niña.filter(Marca__icontains=filtro_marca)
    else:
        ConjuntoLicras_Niña = CNAConjuntoLicraNiña.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'poloversize_dama' or filtro_tipo == 'todos':
        poloversizes_dama = UVpolooversizedama.objects.all()
        if filtro_color:
            poloversizes_dama = poloversizes_dama.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloversizes_dama = poloversizes_dama.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloversizes_dama = poloversizes_dama.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloversizes_dama = poloversizes_dama.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloversizes_dama = poloversizes_dama.filter(Marca__icontains=filtro_marca)
    else:
        poloversizes_dama = UVpolooversizedama.objects.none()
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################
##################################################################1717171 VARON########################################################################################################################

    if filtro_tipo == 'poloversize_varon' or filtro_tipo == 'todos':
        poloversizes_varon = UVpolooversizevaron.objects.all()
        if filtro_color:
            poloversizes_varon = poloversizes_varon.filter(Color__icontains=filtro_color)
        if filtro_diseño:
            poloversizes_varon = poloversizes_varon.filter(Diseño__icontains=filtro_diseño)
        if filtro_codigo:
            poloversizes_varon = poloversizes_varon.filter(Codigo__icontains=filtro_codigo)
        if filtro_talla:
            poloversizes_varon = poloversizes_varon.filter(Talla__icontains=filtro_talla)
        if filtro_marca:
            poloversizes_varon = poloversizes_varon.filter(Marca__icontains=filtro_marca)
    else:
        poloversizes_varon = UVpolooversizevaron.objects.none()


#UVpolooversizedama,UVpolooversizevaron
    context = {
        'licras': licras,
        'novas': novas,
        'interfiles': interfiles,
        'franelas': franelas,
        'elastics': elastics,
        'plushes': plushes,
        'poliesters': poliesters,
        'telas_mojadas': telas_mojadas,
        'polifreshes': polifreshes,
        'lomas': lomas,
        'bosses': bosses,
        'terrys': terrys,
        'franela_plushes': franela_plushes,
        'cortavientos_reversibles': cortavientos_reversibles,
        'cortavientos_reversibles_varones': cortavientos_reversibles_varones,
        'cortavientos_varones' : cortavientos_varones,
        'elastics_varon' : elastics_varon,
        'interfiles_varon' : interfiles_varon,
        'franelas_varon' : franelas_varon,
        'bosses_varon' : bosses_varon,
        'novas_varon' : novas_varon,
        'franelaplushes_varon' : franelaplushes_varon,
        'poliesters_varon' : poliesters_varon,
        'terrys_varon' : terrys_varon,
        'telamojadas_varon' : telamojadas_varon,
        'polifreshes_varon' : polifreshes_varon,
        'pantalonfranelabotarectas_varon' : pantalonfranelabotarectas_varon,
        'pantaloninterfilbotarectas_varon':pantaloninterfilbotarectas_varon,
        'pantalonterrybotarectas_varon' : pantalonterrybotarectas_varon,
        'pantalonnovabotarectas_varon' : pantalonnovabotarectas_varon,
        'pantalonbossebotarectas_varon' : pantalonbossebotarectas_varon,
        'pantaloncortavientobotarectas_varon' : pantaloncortavientobotarectas_varon,
        'joggerterrys_varon' : joggerterrys_varon,
        'joggerfranelas_varon' : joggerfranelas_varon,
        'bividislicras_varon' : bividislicras_varon,
        'casacascortavientos_varon' : casacascortavientos_varon,
        'pantalonetalicras_varon' : pantalonetalicras_varon,
        'poloslicras_varon' : poloslicras_varon,
        'polosalgodones_varon' : polosalgodones_varon,
        'poloscompresor_varon' : poloscompresor_varon,
        'shortelastics_varon' : shortelastics_varon,
        'shortnovas_varon' : shortnovas_varon,
        'shorttelamojadas_varon' : shorttelamojadas_varon,
        'shortterrys_varon' : shortterrys_varon,
        'pantalonesbotarectanova_dama' : pantalonesbotarectanova_dama,
        'pantalonetaslicra_dama' : pantalonetaslicra_dama,
        'joggercargos_dama' : joggercargos_dama,
        'pantalonterrys_dama' : pantalonterrys_dama,
        'pantalonlicrabotarectas_dama' : pantalonlicrabotarectas_dama,
        'pantaloninterfils_dama' : pantaloninterfils_dama,
        'pantalonfranelas_dama' : pantalonfranelas_dama,
        'pantalonlomas_dama' : pantalonlomas_dama,
        'joggerinterfils_dama' :joggerinterfils_dama,
        'joggerbotapiefranelas_dama':joggerbotapiefranelas_dama,
        'joggerbotapieterrys_dama' : joggerbotapieterrys_dama,
        'joggeroversizeterrys_dama':joggeroversizeterrys_dama,
        'pantalonpalazosdama':pantalonpalazosdama,
        'pantalonetaterrys_dama' : pantalonetaterrys_dama,
        'joggeroversizefranelas_dama' : joggeroversizefranelas_dama,
        'poloslicramangalarga_dama' : poloslicramangalarga_dama,
        'pololicrasmangacorta_dama' : pololicrasmangacorta_dama,
        'poloscroplicra_dama' : poloscroplicra_dama,
        'shortslicra_dama' : shortslicra_dama,
        'faldashortslicra_dama' : faldashortslicra_dama,
        'bikerslicra_dama' : bikerslicra_dama,
        'snikerslicra_dama' : snikerslicra_dama,
        'shortterrys_dama' : shortterrys_dama,
        'shortnovasdama' : shortnovasdama,
        'shorttelamojadas_dama': shorttelamojadas_dama,
        'poloalgodonmangalargas_dama' : poloalgodonmangalargas_dama,
        'poloalgodonmangacortas_dama' : poloalgodonmangacortas_dama,
        'polocuellocamiseros_dama' : polocuellocamiseros_dama,
        'casacalicras_dama' : casacalicras_dama,
        'casacacortavientos_dama' : casacacortavientos_dama,
        'tops_dama': tops_dama,
        'bividis_dama' : bividis_dama,
        'enterizos_dama' : enterizos_dama,
        'ConjuntoNovas_Niño':ConjuntoNovas_Niño,
        'ConjuntoNovas_Niña':ConjuntoNovas_Niña,
        'ConjuntoInterfils_Niño' : ConjuntoInterfils_Niño,
        'ConjuntoLicras_Niña' : ConjuntoLicras_Niña,
        'poloversizes_dama' :poloversizes_dama,
        'poloversizes_varon' : poloversizes_varon,
        'filtro_tipo': filtro_tipo,
        'filtro_color': filtro_color,
        'filtro_diseño': filtro_diseño,
        'filtro_codigo': filtro_codigo,
        'filtro_talla': filtro_codigo,
        'filtro_marca': filtro_marca,
    }
    return render(request, 'crud_productos/listar_productos.html', context)
















































##############################################################################################
##############################################################################################
##############################################################################################
from .models import Ventas_Mensuale2  # Asegúrate de importar ambos modelos



def index(request):
    # Datos para Ventas_Mensuale
    ventas_diarias = Ventas_Mensuale.objects.values('fecha').annotate(
        total_dia=Sum('monto')
    ).order_by('fecha')

    ventas_por_mes = defaultdict(list)
    for venta in ventas_diarias:
        fecha = venta['fecha']
        total_dia = venta['total_dia']
        mes = DateFormat(fecha).format('Y-m')
        ventas_por_mes[mes].append({'fecha': DateFormat(fecha).format('d M Y'), 'total_dia': float(total_dia)})

    meses = sorted(ventas_por_mes.keys())
    data_por_mes = [{'mes': mes, 'labels': [venta['fecha'] for venta in ventas_por_mes[mes]], 'data': [venta['total_dia'] for venta in ventas_por_mes[mes]]} for mes in meses]

    # Datos para Ventas_Mensuale2
    ventas_diarias2 = Ventas_Mensuale2.objects.values('fecha').annotate(
        total_dia=Sum('monto')
    ).order_by('fecha')

    ventas_por_mes2 = defaultdict(list)
    for venta in ventas_diarias2:
        fecha = venta['fecha']
        total_dia = venta['total_dia']
        mes = DateFormat(fecha).format('Y-m')
        ventas_por_mes2[mes].append({'fecha': DateFormat(fecha).format('d M Y'), 'total_dia': float(total_dia)})

    meses2 = sorted(ventas_por_mes2.keys())
    data_por_mes2 = [{'mes': mes, 'labels': [venta['fecha'] for venta in ventas_por_mes2[mes]], 'data': [venta['total_dia'] for venta in ventas_por_mes2[mes]]} for mes in meses2]

    context = {
        'data_por_mes': data_por_mes,
        'data_por_mes2': data_por_mes2,  # Añade los datos de Ventas_Mensuale2
    }

    return render(request, 'index.html', context)







#########################################################################
from django.utils.dateparse import parse_date


def ventas(request):
    ventas = Venta.objects.all()
    
    fecha = request.GET.get('fecha')  # Obtener la fecha seleccionada del formulario
    if fecha:
        fecha_filtrada = parse_date(fecha)
        if fecha_filtrada:
            ventas = ventas.filter(fecha__date=fecha_filtrada)  # Filtrar ventas por fecha

    return render(request, 'crud_ventas/ventas.html', {'ventas': ventas, 'fecha': fecha})





def agregar_venta(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        metodo_pago = request.POST.get('metodo_pago')
        estado = request.POST.get('estado')
        
        venta = Venta(
            descripcion=descripcion,
            monto=monto,
            metodo_pago=metodo_pago,
            estado=estado,
            fecha=timezone.now()
        )
        venta.save()
        return redirect('ventas')
    
    return render(request, 'crud_ventas/agregar_venta.html')


def editar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.descripcion = request.POST.get('descripcion')
        venta.monto = request.POST.get('monto')
        venta.metodo_pago = request.POST.get('metodo_pago')
        venta.estado = request.POST.get('estado')
        venta.save()
        return redirect('ventas')
    
    return render(request, 'crud_ventas/editar_venta.html', {'venta': venta})
###############################################################
###############################################################
###############################################################
###############################################################

def ventas2(request):

    ventas = Venta2.objects.all()
    
    fecha = request.GET.get('fecha')  # Obtener la fecha seleccionada del formulario
    if fecha:
        fecha_filtrada = parse_date(fecha)
        if fecha_filtrada:
            ventas = ventas.filter(fecha__date=fecha_filtrada)  # Filtrar ventas por fecha

    return render(request, 'crud_ventas/ventas2.html', {'ventas': ventas, 'fecha': fecha})



def agregar_venta2(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        metodo_pago = request.POST.get('metodo_pago')
        estado = request.POST.get('estado')
        
        venta = Venta2(
            descripcion=descripcion,
            monto=monto,
            metodo_pago=metodo_pago,
            estado=estado,
            fecha=timezone.now()
        )
        venta.save()
        return redirect('ventas2')
    
    return render(request, 'crud_ventas/agregar_venta2.html')

def editar_venta2(request, id):
    venta = get_object_or_404(Venta2, id=id)
    if request.method == 'POST':
        venta.descripcion = request.POST.get('descripcion')
        venta.monto = request.POST.get('monto')
        venta.metodo_pago = request.POST.get('metodo_pago')
        venta.estado = request.POST.get('estado')
        venta.save()
        return redirect('ventas2')
    
    return render(request, 'crud_ventas/editar_venta2.html', {'venta': venta})















###############################################################
###############################################################
###############################################################
###############################################################
def listar (request):
    tareas = Tareas.objects.all()
    return render(request,'crud_tareas/listar.html',{'tareas':tareas })

def agregar (request):
    return render(request,'crud_tareas/agregar.html')

def actualizar (request):
    return render(request,'crud_tareas/actualizar.html')

def eliminar (request):
    return render(request,'crud_tareas/eliminar.html')


###############################################################


###############################################################
def clientes(request):
    tareas = Cliente.objects.all()
    
    # Obtener valores de los filtros
    dni_filtro = request.GET.get('dni')
    
    # Aplicar filtros si están presentes
    if dni_filtro:
        tareas = tareas.filter(dni=dni_filtro)

    dnis = Cliente.objects.values_list('dni', flat=True).distinct()

    context = {
        'tareas': tareas,
        'dnis': dnis,
    }
    return render(request, 'crud_clientes/listar_cliente.html', context)



def inventario_personal(request):
    return render(request, 'inventario_personal/inventario_personal.html')




###############################################################
###############################################################
###############################################################

from .forms import ClienteForm

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')  # Redirigir a la lista de clientes después de añadir uno nuevo
    else:
        form = ClienteForm()
    
    return render(request, 'crud_clientes/agregar_cliente.html', {'form': form})


def editar_cliente(request, dni):
    cliente = get_object_or_404(Cliente, dni=dni)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')  # Redirigir a la lista de clientes después de editar uno
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'crud_clientes/editar_cliente.html', {'form': form, 'cliente': cliente})
###############################################################
###############################################################
###############################################################
def pedido_cdlicra (request):
    tareas = ConjuntosLicraDama.objects.all()

    # Obtener valores de los filtros
    color_filtro = request.GET.get('color')
    talla_filtro = request.GET.get('talla')
    marca_filtro = request.GET.get('marca')

    # Aplicar filtros si están presentes
    if color_filtro:
        tareas = tareas.filter(Color=color_filtro)
    if talla_filtro:
        tareas = tareas.filter(Talla=talla_filtro)
    if marca_filtro:
        tareas = tareas.filter(Marca=marca_filtro)

    # Obtener valores únicos para los filtros
    colores = ConjuntosLicraDama.objects.values_list('Color', flat=True).distinct()
    tallas = ConjuntosLicraDama.objects.values_list('Talla', flat=True).distinct()
    marcas = ConjuntosLicraDama.objects.values_list('Marca', flat=True).distinct()

    context = {
        'tareas': tareas,
        'colores': colores,
        'tallas': tallas,
        'marcas': marcas,
    }

    return render(request, 'crud_conjuntolicradama/pedido.html', context)

def listar_cdlicra(request):
    tareas = ConjuntosLicraDama.objects.all()

    # Obtener valores de los filtros
    color_filtro = request.GET.get('color')
    talla_filtro = request.GET.get('talla')
    marca_filtro = request.GET.get('marca')
    codigo_filtro = request.GET.get('marca')
    # Aplicar filtros si están presentes
    if color_filtro:
        tareas = tareas.filter(Color=color_filtro)
    if talla_filtro:
        tareas = tareas.filter(Talla=talla_filtro)
    if marca_filtro:
        tareas = tareas.filter(Marca=marca_filtro)
    if codigo_filtro:
        tareas = tareas.filter(Codigo=codigo_filtro)

    # Obtener valores únicos para los filtros
    colores = ConjuntosLicraDama.objects.values_list('Color', flat=True).distinct()
    tallas = ConjuntosLicraDama.objects.values_list('Talla', flat=True).distinct()
    marcas = ConjuntosLicraDama.objects.values_list('Marca', flat=True).distinct()
    codigos = ConjuntosLicraDama.objects.values_list('Codigo', flat=True).distinct()

    context = {
        'tareas': tareas,
        'colores': colores,
        'tallas': tallas,
        'marcas': marcas,
        'codigos': codigos,
    }

    return render(request, 'crud_conjuntolicradama/listar.html', context)



#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################


###############################################################
def pedido_cdnova (request):
    tareas = ConjuntosNovaDama.objects.all()

    # Obtener valores de los filtros
    color_filtro = request.GET.get('color')
    talla_filtro = request.GET.get('talla')
    marca_filtro = request.GET.get('marca')

    # Aplicar filtros si están presentes
    if color_filtro:
        tareas = tareas.filter(Color=color_filtro)
    if talla_filtro:
        tareas = tareas.filter(Talla=talla_filtro)
    if marca_filtro:
        tareas = tareas.filter(Marca=marca_filtro)

    # Obtener valores únicos para los filtros
    colores = ConjuntosLicraDama.objects.values_list('Color', flat=True).distinct()
    tallas = ConjuntosLicraDama.objects.values_list('Talla', flat=True).distinct()
    marcas = ConjuntosLicraDama.objects.values_list('Marca', flat=True).distinct()

    context = {
        'tareas': tareas,
        'colores': colores,
        'tallas': tallas,
        'marcas': marcas,
    }

    return render(request, 'crud_conjuntonovadama/pedido.html', context)

def listar_cdnova(request):
    tareas = ConjuntosNovaDama.objects.all()

    # Obtener valores de los filtros
    color_filtro = request.GET.get('color')
    talla_filtro = request.GET.get('talla')
    marca_filtro = request.GET.get('marca')
    codigo_filtro = request.GET.get('marca')
    # Aplicar filtros si están presentes
    if color_filtro:
        tareas = tareas.filter(Color=color_filtro)
    if talla_filtro:
        tareas = tareas.filter(Talla=talla_filtro)
    if marca_filtro:
        tareas = tareas.filter(Marca=marca_filtro)
    if codigo_filtro:
        tareas = tareas.filter(Codigo=codigo_filtro)

    # Obtener valores únicos para los filtros
    colores = ConjuntosNovaDama.objects.values_list('Color', flat=True).distinct()
    tallas = ConjuntosNovaDama.objects.values_list('Talla', flat=True).distinct()
    marcas = ConjuntosNovaDama.objects.values_list('Marca', flat=True).distinct()
    codigos = ConjuntosNovaDama.objects.values_list('Codigo', flat=True).distinct()

    context = {
        'tareas': tareas,
        'colores': colores,
        'tallas': tallas,
        'marcas': marcas,
        'codigos': codigos,
    }

    return render(request, 'crud_conjuntonovadama/listar.html', context)


#def inventario_personal(request):
#        total_s1 = ConjuntosLicraDama.objects.aggregate(Sum('S1'))['S1__sum']
#        total_s2 = ConjuntosLicraDama.objects.aggregate(Sum('S2'))['S2__sum']
    
#        context = {
#            'total_s1': total_s1,
#            'total_s2': total_s2,
#            }
#        return render(request, 'inventario_personal.html', context)