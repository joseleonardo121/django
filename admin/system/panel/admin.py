from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from .models import Tareas,Cliente,Venta,Ventas_Mensuale,Venta2,ReportesGenerales,Ventas_Mensuale2,TiendaArchivo,UVpolooversizedama,UVpolooversizevaron
from .models import ConjuntosLicraDama,ConjuntosNovaDama,ConjuntosInterfilDama,ConjuntosFranelaDama,ConjuntosElasticDama,ConjuntosPlushDama,ConjuntosPoliesterDama,ConjuntosPolifreshDama,ConjuntosTelaMojadaDama,ConjuntosBosseDama,ConjuntosCortavientoReversibleDama,ConjuntosFranelaPLushDama,ConjuntosTerryDama,ConjuntosLomaDama
from .models import CNOConjuntoNovaNiño,CNOConjuntoInterfilNiño,CNAConjuntoNovaNiña,CNAConjuntoLicraNiña,UDpantalonpalazodama
from .models import UNOPantalonNiño,InventariodeTotales

@admin.register(Ventas_Mensuale)
class VentasMensualesAdmin(admin.ModelAdmin):
    list_display = ('fecha','monto',)

@admin.register(TiendaArchivo)
class TiendaArchivoAdmin(admin.ModelAdmin):
    list_display = ('archivo','tienda1','tienda2','Ganancia_Tienda1','Ganancia_Tienda2','Ganancia_Total')

@admin.register(Ventas_Mensuale2)
class VentasMensuales2Admin(admin.ModelAdmin):
    list_display = ('fecha','monto',)

@admin.register(Tareas)
class TareasAdmin(admin.ModelAdmin):
    list_display = ('id','tienda','descripcion','f_registro','realizado',)
    ordering = ('id',)
    list_filter=('tienda',)
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellido','celular',)

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
    
class VentaAdmin(admin.ModelAdmin):
    list_display = ('numero_ticket', 'descripcion', 'monto', 'metodo_pago', 'fecha', 'estado')
    list_filter = ('metodo_pago', 'estado', 'fecha')
    search_fields = ('fecha',)
    list_editable = ('estado',)

admin.site.register(Venta, VentaAdmin)
###################################################################

class Venta2Admin(admin.ModelAdmin):
    list_display = ('numero_ticket', 'descripcion', 'monto', 'metodo_pago', 'fecha', 'estado')
    list_filter = ('metodo_pago', 'estado', 'fecha')
    search_fields = ('fecha', 'descripcion')
    list_editable = ('estado',)

admin.site.register(Venta2, Venta2Admin)

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
@admin.register(CNOConjuntoNovaNiño)
class CNOConjuntoNovaNiñoAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)
####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in CNOConjuntoNovaNiño.objects.all()))- (sum(producto.inversion() for producto in CNOConjuntoNovaNiño.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in CNOConjuntoNovaNiño.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################
@admin.register(CNOConjuntoInterfilNiño)
class CNOConjuntoInterfilNiñoAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)
####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in CNOConjuntoInterfilNiño.objects.all()))- (sum(producto.inversion() for producto in CNOConjuntoInterfilNiño.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in CNOConjuntoInterfilNiño.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UNOPantalonNiño)
class UNOPantalonNiñoAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)
####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UNOPantalonNiño.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UNOPantalonNiño.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UNOPantalonNiño.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UNOPantalonNiño.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UNOPantalonNiño.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UNOPantalonNiño.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UNOPantalonNiño.objects.all()))- (sum(producto.inversion() for producto in UNOPantalonNiño.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UNOPantalonNiño.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UNOPantalonNiño.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UNOPantalonNiño.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UNOPantalonNiño.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UNOPantalonNiño.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())










###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
@admin.register(CNAConjuntoNovaNiña)
class CNAConjuntoNovaNiñaAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)
####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in CNAConjuntoNovaNiña.objects.all()))- (sum(producto.inversion() for producto in CNAConjuntoNovaNiña.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in CNAConjuntoNovaNiña.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
@admin.register(CNAConjuntoLicraNiña)
class CNAConjuntoLicraNiñaAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)
####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in CNAConjuntoLicraNiña.objects.all()))- (sum(producto.inversion() for producto in CNAConjuntoLicraNiña.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in CNAConjuntoLicraNiña.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())















###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
@admin.register(ConjuntosLicraDama)
class ConjuntosLicraDamaAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)
####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosLicraDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosLicraDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosLicraDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosLicraDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosLicraDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosLicraDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosLicraDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosLicraDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosLicraDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosLicraDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosLicraDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosLicraDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosLicraDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())
    
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################


@admin.register(ConjuntosNovaDama)
class ConjuntosNovaDamaAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosNovaDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosNovaDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosNovaDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosNovaDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosNovaDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosNovaDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosNovaDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosNovaDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosNovaDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosNovaDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosNovaDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosNovaDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosNovaDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


#########################################################################################################################################################################################################
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################
#########################################################################################################################################################################################################




@admin.register(ConjuntosInterfilDama)
class ConjuntosInterfilDamaAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosInterfilDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosInterfilDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosInterfilDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosInterfilDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosInterfilDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosInterfilDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosInterfilDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosInterfilDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosInterfilDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosInterfilDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosInterfilDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosInterfilDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosInterfilDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosFranelaDama)
class ConjuntosFranelaDamaAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosFranelaDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosFranelaDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosFranelaDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosFranelaDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosFranelaDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosFranelaDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosFranelaDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosFranelaDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosFranelaDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosFranelaDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosFranelaDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosFranelaDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosFranelaDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosElasticDama)
class ConjuntosElasticDamaAdmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Modelo','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosElasticDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosElasticDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosElasticDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosElasticDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosElasticDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosElasticDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosElasticDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosElasticDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosElasticDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosElasticDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosElasticDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosElasticDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosElasticDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())
    

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosPoliesterDama)
class ConjuntosPoliesterDamadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosPoliesterDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosPoliesterDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosPoliesterDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosPoliesterDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosPoliesterDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosPoliesterDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosPoliesterDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosPoliesterDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosPoliesterDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosPoliesterDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosPoliesterDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosPoliesterDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosPoliesterDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosTelaMojadaDama)
class ConjuntosTelaMojadaDamadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosTelaMojadaDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosTelaMojadaDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosTelaMojadaDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosPolifreshDama)
class ConjuntosPolifreshDamadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosPolifreshDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosPolifreshDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosPolifreshDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosPolifreshDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosPolifreshDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosPolifreshDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosPolifreshDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosPolifreshDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosPolifreshDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosPolifreshDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosPolifreshDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosPolifreshDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosPolifreshDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosPlushDama)
class ConjuntosPlushDamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Modelo','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosPlushDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosPlushDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosPlushDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosPlushDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosPlushDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosPlushDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosPlushDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosPlushDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosPlushDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosPlushDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosPlushDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosPlushDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosPlushDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosFranelaPLushDama)
class ConjuntosFranelaPLushDamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosFranelaPLushDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosFranelaPLushDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosFranelaPLushDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosTerryDama)
class ConjuntosTerryDamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Modelo','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosTerryDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosTerryDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosTerryDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosTerryDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosTerryDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosTerryDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosTerryDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosTerryDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosTerryDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosTerryDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosTerryDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosTerryDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosTerryDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosCortavientoReversibleDama)
class ConjuntosCortavientoReversibleDamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosCortavientoReversibleDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosCortavientoReversibleDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosCortavientoReversibleDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(ConjuntosBosseDama)
class ConjuntosBosseDamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosBosseDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosBosseDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosBosseDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosBosseDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosBosseDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosBosseDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosBosseDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosBosseDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosBosseDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosBosseDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosBosseDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosBosseDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosBosseDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(ConjuntosLomaDama)
class ConjuntosLomaDamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosLomaDama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosLomaDama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosLomaDama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosLomaDama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosLomaDama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosLomaDama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosLomaDama.objects.all()))- (sum(producto.inversion() for producto in ConjuntosLomaDama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosLomaDama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosLomaDama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosLomaDama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosLomaDama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosLomaDama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())
    

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

from . models import ConjuntosCortavientoReversibleVaron,ConjuntosCortavientoVaron,ConjuntosElasticVaron,ConjuntosFranelaVaron,ConjuntosInterfilVaron,ConjuntosBosseVaron,ConjuntosNovaVaron,ConjuntosFranelaPlushVaron,ConjuntosPoliesterVaron,ConjuntosPolifreshVaron,ConjuntosTelaMojadaVaron,ConjuntosTerryVaron

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosCortavientoReversibleVaron)
class ConjuntosCortavientoReversibleVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosCortavientoReversibleVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosCortavientoReversibleVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosCortavientoReversibleVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(ConjuntosCortavientoVaron)
class ConjuntosCortavientoVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosCortavientoVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosCortavientoVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosCortavientoVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosElasticVaron)
class ConjuntosElasticVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosElasticVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosElasticVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosElasticVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosElasticVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosElasticVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosElasticVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosElasticVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosElasticVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosElasticVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosElasticVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosElasticVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosElasticVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosElasticVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(ConjuntosFranelaVaron)
class ConjuntosFranelaVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Modelo','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosFranelaVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosFranelaVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosFranelaVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosFranelaVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosFranelaVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosFranelaVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosFranelaVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosFranelaVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosFranelaVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosFranelaVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosFranelaVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosFranelaVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosFranelaVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(ConjuntosInterfilVaron)
class ConjuntosInterfilVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosInterfilVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosInterfilVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosInterfilVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosInterfilVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosInterfilVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosInterfilVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosInterfilVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosInterfilVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosInterfilVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosInterfilVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosInterfilVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosInterfilVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosInterfilVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosBosseVaron)
class ConjuntosBosseVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosBosseVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosBosseVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosBosseVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosBosseVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosBosseVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosBosseVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosBosseVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosBosseVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosBosseVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosBosseVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosBosseVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosBosseVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosBosseVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(ConjuntosNovaVaron)
class ConjuntosNovaVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosNovaVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosNovaVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosNovaVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosNovaVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosNovaVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosNovaVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosNovaVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosNovaVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosNovaVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosNovaVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosNovaVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosNovaVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosNovaVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosFranelaPlushVaron)
class ConjuntosFranelaPlushVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosFranelaPlushVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosFranelaPlushVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosFranelaPlushVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosPoliesterVaron)
class ConjuntosFranelaPlushVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosPoliesterVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosPoliesterVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosPoliesterVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(ConjuntosPolifreshVaron)
class ConjuntosPolifreshVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosPolifreshVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosPolifreshVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosPolifreshVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosTelaMojadaVaron)
class ConjuntosTelaMojadaVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosTelaMojadaVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosTelaMojadaVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosTelaMojadaVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(ConjuntosTerryVaron)
class ConjuntosTerryVaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Modelo','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in ConjuntosTerryVaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in ConjuntosTerryVaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in ConjuntosTerryVaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in ConjuntosTerryVaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in ConjuntosTerryVaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in ConjuntosTerryVaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in ConjuntosTerryVaron.objects.all()))- (sum(producto.inversion() for producto in ConjuntosTerryVaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in ConjuntosTerryVaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in ConjuntosTerryVaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in ConjuntosTerryVaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in ConjuntosTerryVaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in ConjuntosTerryVaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

from . models import UVPantalonFranelaBotaRecta,UVPantalonInterfilBotaRecta,UVPantalonNovaBotaRecta,UVPantalonTerryBotaRecta,UVPantalonbossebotaRecta,UVPantaloncortavientobotaRecta,UVPantalonfranelabotajogger,UVPantalonterrybotajogger,UVBividilicravaron,UVcasacascortavientovaron,UVPantalonetaslicravaron,UVPpoloalgodonvaron,UVPpolocompresorvaron,UVPpololicravaron,UVshortelasticvaron,UVshortnovavaron,UVshorttelamojadavaron,UVshortterryvaron
@admin.register(UVpolooversizevaron)
class UVpolooversizevarondmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVpolooversizevaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVpolooversizevaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVpolooversizevaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVpolooversizevaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVpolooversizevaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVpolooversizevaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVpolooversizevaron.objects.all()))- (sum(producto.inversion() for producto in UVpolooversizevaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVpolooversizevaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVpolooversizevaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVpolooversizevaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVpolooversizevaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVpolooversizevaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UVPantalonFranelaBotaRecta)
class UVPantalonFranelaBotaRectaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonFranelaBotaRecta.objects.all()))- (sum(producto.inversion() for producto in UVPantalonFranelaBotaRecta.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonFranelaBotaRecta.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################




@admin.register(UVPantalonInterfilBotaRecta)
class UVPantalonInterfilBotaRectaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonInterfilBotaRecta.objects.all()))- (sum(producto.inversion() for producto in UVPantalonInterfilBotaRecta.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonInterfilBotaRecta.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UVPantalonNovaBotaRecta)
class UVPantalonNovaBotaRectaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonNovaBotaRecta.objects.all()))- (sum(producto.inversion() for producto in UVPantalonNovaBotaRecta.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonNovaBotaRecta.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVPantalonTerryBotaRecta)
class UVPantalonTerryBotaRectaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonTerryBotaRecta.objects.all()))- (sum(producto.inversion() for producto in UVPantalonTerryBotaRecta.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonTerryBotaRecta.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())





###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UVPantaloncortavientobotaRecta)
class UVPantaloncortavientobotaRectaaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color','Modelo',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantaloncortavientobotaRecta.objects.all()))- (sum(producto.inversion() for producto in UVPantaloncortavientobotaRecta.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantaloncortavientobotaRecta.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVPantalonbossebotaRecta)
class UVPantalonbossebotaRectaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonbossebotaRecta.objects.all()))- (sum(producto.inversion() for producto in UVPantalonbossebotaRecta.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonbossebotaRecta.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVPantalonfranelabotajogger)
class UVPantalonfranelabotajoggeradmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonfranelabotajogger.objects.all()))- (sum(producto.inversion() for producto in UVPantalonfranelabotajogger.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonfranelabotajogger.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())




###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVPantalonterrybotajogger)
class UVPantalonterrybotajoggeradmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonterrybotajogger.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonterrybotajogger.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonterrybotajogger.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonterrybotajogger.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonterrybotajogger.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonterrybotajogger.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonterrybotajogger.objects.all()))- (sum(producto.inversion() for producto in UVPantalonterrybotajogger.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonterrybotajogger.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonterrybotajogger.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonterrybotajogger.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonterrybotajogger.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonterrybotajogger.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())
    


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVBividilicravaron)
class UVBividilicravaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color')

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVBividilicravaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVBividilicravaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVBividilicravaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVBividilicravaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVBividilicravaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVBividilicravaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVBividilicravaron.objects.all()))- (sum(producto.inversion() for producto in UVBividilicravaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVBividilicravaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVBividilicravaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVBividilicravaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVBividilicravaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVBividilicravaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



#    #,,UVPantalonetaslicravaron


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVcasacascortavientovaron)
class UVcasacascortavientovaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVcasacascortavientovaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVcasacascortavientovaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVcasacascortavientovaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVcasacascortavientovaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVcasacascortavientovaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVcasacascortavientovaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVcasacascortavientovaron.objects.all()))- (sum(producto.inversion() for producto in UVcasacascortavientovaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVcasacascortavientovaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVcasacascortavientovaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVcasacascortavientovaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVcasacascortavientovaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVcasacascortavientovaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())




###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UVPantalonetaslicravaron)
class UVPantalonetaslicravaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPantalonetaslicravaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPantalonetaslicravaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPantalonetaslicravaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPantalonetaslicravaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPantalonetaslicravaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPantalonetaslicravaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPantalonetaslicravaron.objects.all()))- (sum(producto.inversion() for producto in UVPantalonetaslicravaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPantalonetaslicravaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPantalonetaslicravaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPantalonetaslicravaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPantalonetaslicravaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPantalonetaslicravaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())





###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UVPpoloalgodonvaron)
class UVPpoloalgodonvaronnadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPpoloalgodonvaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPpoloalgodonvaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPpoloalgodonvaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPpoloalgodonvaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPpoloalgodonvaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPpoloalgodonvaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPpoloalgodonvaron.objects.all()))- (sum(producto.inversion() for producto in UVPpoloalgodonvaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPpoloalgodonvaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPpoloalgodonvaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPpoloalgodonvaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPpoloalgodonvaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPpoloalgodonvaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())





#,UVPpolocompresorvaron,


###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UVPpololicravaron)
class UVPpololicravaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPpololicravaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPpololicravaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPpololicravaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPpololicravaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPpololicravaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPpololicravaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPpololicravaron.objects.all()))- (sum(producto.inversion() for producto in UVPpololicravaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPpololicravaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPpololicravaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPpololicravaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPpololicravaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPpololicravaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVPpolocompresorvaron)
class UVPpolocompresorvarondmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Modelo','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVPpolocompresorvaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVPpolocompresorvaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVPpolocompresorvaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVPpolocompresorvaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVPpolocompresorvaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVPpolocompresorvaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVPpolocompresorvaron.objects.all()))- (sum(producto.inversion() for producto in UVPpolocompresorvaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVPpolocompresorvaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVPpolocompresorvaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVPpolocompresorvaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVPpolocompresorvaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVPpolocompresorvaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVshortnovavaron)
class UVshortnovavaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVshortnovavaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVshortnovavaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVshortnovavaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVshortnovavaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVshortnovavaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVshortnovavaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVshortnovavaron.objects.all()))- (sum(producto.inversion() for producto in UVshortnovavaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVshortnovavaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVshortnovavaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVshortnovavaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVshortnovavaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVshortnovavaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

##,,

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVshorttelamojadavaron)
class UVshorttelamojadavaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVshorttelamojadavaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVshorttelamojadavaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVshorttelamojadavaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVshorttelamojadavaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVshorttelamojadavaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVshorttelamojadavaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVshorttelamojadavaron.objects.all()))- (sum(producto.inversion() for producto in UVshorttelamojadavaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVshorttelamojadavaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVshorttelamojadavaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVshorttelamojadavaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVshorttelamojadavaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVshorttelamojadavaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVshortterryvaron)
class UVshortterryvaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVshortterryvaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVshortterryvaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVshortterryvaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVshortterryvaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVshortterryvaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVshortterryvaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVshortterryvaron.objects.all()))- (sum(producto.inversion() for producto in UVshortterryvaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVshortterryvaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVshortterryvaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVshortterryvaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVshortterryvaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVshortterryvaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UVshortelasticvaron)
class UVshortelasticvaronadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVshortelasticvaron.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVshortelasticvaron.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVshortelasticvaron.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVshortelasticvaron.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVshortelasticvaron.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVshortelasticvaron.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVshortelasticvaron.objects.all()))- (sum(producto.inversion() for producto in UVshortelasticvaron.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVshortelasticvaron.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVshortelasticvaron.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVshortelasticvaron.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVshortelasticvaron.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVshortelasticvaron.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

from . models import UDpantalonetalicradama,UDpantalonnovabotarectadama,UDjoggercargodama,UDpantalonfraneladama,UDpantaloninterfildama,UDpantalonlicrabotarectadama,UDpantalonlomadama,UDpantalonterrydama,UDjoggerbotapiefraneladama,UDjoggerbotapieterrydama,UDjoggerinterfildama,UDjoggeroversizefraneladama,UDjoggeroversizeterrydama,UDpantalonetaterrydama,UDpolocroplicradama,UDpololicramangacortadama,UDpololicramangalargadama,UDbikerlicradama,UDfaldashortdama,UDshortlicradama,UDsnikerlicradama,UDbivididama,UDtopdama,UDenterizodama


###################################################################
###################################################################
###################################################################
###################################################################
@admin.register(UVpolooversizedama)
class UVpolooversizedamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UVpolooversizedama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UVpolooversizedama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UVpolooversizedama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UVpolooversizedama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UVpolooversizedama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UVpolooversizedama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UVpolooversizedama.objects.all()))- (sum(producto.inversion() for producto in UVpolooversizedama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UVpolooversizedama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UVpolooversizedama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UVpolooversizedama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UVpolooversizedama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UVpolooversizedama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())





###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UDpantalonetalicradama)
class UDpantalonetalicradamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonetalicradama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonetalicradama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonetalicradama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonetalicradama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonetalicradama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonetalicradama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonetalicradama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonetalicradama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonetalicradama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonetalicradama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonetalicradama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonetalicradama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonetalicradama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())





###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpantalonnovabotarectadama)
class UDpantalonnovabotarectadamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonnovabotarectadama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonnovabotarectadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonnovabotarectadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpantalonpalazodama)
class UDpantalonpalazodamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonpalazodama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonpalazodama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonpalazodama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonpalazodama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonpalazodama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonpalazodama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonpalazodama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonpalazodama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonpalazodama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonpalazodama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonpalazodama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonpalazodama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonpalazodama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDjoggercargodama)
class UDjoggercargodamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDjoggercargodama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDjoggercargodama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDjoggercargodama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDjoggercargodama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDjoggercargodama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDjoggercargodama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDjoggercargodama.objects.all()))- (sum(producto.inversion() for producto in UDjoggercargodama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDjoggercargodama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDjoggercargodama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDjoggercargodama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDjoggercargodama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDjoggercargodama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())






###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDpantalonterrydama)
class UDpantalonterrydamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonterrydama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonterrydama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonterrydama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonterrydama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonterrydama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonterrydama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonterrydama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonterrydama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonterrydama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonterrydama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonterrydama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())




###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpantalonfraneladama)
class UDpantalonfraneladamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonfraneladama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonfraneladama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonfraneladama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonfraneladama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonfraneladama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonfraneladama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonfraneladama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonfraneladama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonfraneladama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonfraneladama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonfraneladama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonfraneladama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonfraneladama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())




###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpantalonlicrabotarectadama)
class UDpantalonlicrabotarectadamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonlicrabotarectadama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonlicrabotarectadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonlicrabotarectadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpantalonlomadama)
class UDpantalonlomadamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonlomadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonlomadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonlomadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonlomadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonlomadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonlomadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonlomadama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonlomadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonlomadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonlomadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonlomadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonlomadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonlomadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpantaloninterfildama)
class UDpantaloninterfildamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantaloninterfildama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantaloninterfildama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantaloninterfildama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantaloninterfildama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantaloninterfildama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantaloninterfildama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantaloninterfildama.objects.all()))- (sum(producto.inversion() for producto in UDpantaloninterfildama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantaloninterfildama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantaloninterfildama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantaloninterfildama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantaloninterfildama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantaloninterfildama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDjoggerbotapiefraneladama)
class UDpantaloninterfildamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDjoggerbotapiefraneladama.objects.all()))- (sum(producto.inversion() for producto in UDjoggerbotapiefraneladama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDjoggerbotapiefraneladama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDjoggerbotapieterrydama)
class UDjoggerbotapieterrydamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDjoggerbotapieterrydama.objects.all()))- (sum(producto.inversion() for producto in UDjoggerbotapieterrydama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDjoggerbotapieterrydama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UDjoggerinterfildama)
class UDjoggerinterfildamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDjoggerinterfildama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDjoggerinterfildama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDjoggerinterfildama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDjoggerinterfildama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDjoggerinterfildama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDjoggerinterfildama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDjoggerinterfildama.objects.all()))- (sum(producto.inversion() for producto in UDjoggerinterfildama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDjoggerinterfildama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDjoggerinterfildama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDjoggerinterfildama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDjoggerinterfildama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDjoggerinterfildama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDjoggeroversizefraneladama)
class UDjoggeroversizefraneladamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDjoggeroversizefraneladama.objects.all()))- (sum(producto.inversion() for producto in UDjoggeroversizefraneladama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDjoggeroversizefraneladama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDjoggeroversizeterrydama)
class UDjoggeroversizeterrydamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDjoggeroversizeterrydama.objects.all()))- (sum(producto.inversion() for producto in UDjoggeroversizeterrydama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDjoggeroversizeterrydama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpantalonetaterrydama)
class UDpantalonetaterrydamaaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpantalonetaterrydama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpantalonetaterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpantalonetaterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpantalonetaterrydama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpantalonetaterrydama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpantalonetaterrydama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpantalonetaterrydama.objects.all()))- (sum(producto.inversion() for producto in UDpantalonetaterrydama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpantalonetaterrydama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpantalonetaterrydama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpantalonetaterrydama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpantalonetaterrydama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpantalonetaterrydama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())



###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpolocroplicradama)
class UDpolocroplicradamaaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Modelo','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpolocroplicradama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpolocroplicradama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpolocroplicradama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpolocroplicradama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpolocroplicradama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpolocroplicradama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpolocroplicradama.objects.all()))- (sum(producto.inversion() for producto in UDpolocroplicradama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpolocroplicradama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpolocroplicradama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpolocroplicradama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpolocroplicradama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpolocroplicradama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())




###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDpololicramangacortadama)
class UDpololicramangacortadamaaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpololicramangacortadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpololicramangacortadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpololicramangacortadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpololicramangacortadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpololicramangacortadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpololicramangacortadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpololicramangacortadama.objects.all()))- (sum(producto.inversion() for producto in UDpololicramangacortadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpololicramangacortadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpololicramangacortadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpololicramangacortadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpololicramangacortadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpololicramangacortadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UDpololicramangalargadama)
class UDpololicramangalargadamaaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Diseño','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpololicramangalargadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpololicramangalargadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpololicramangalargadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpololicramangalargadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpololicramangalargadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpololicramangalargadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpololicramangalargadama.objects.all()))- (sum(producto.inversion() for producto in UDpololicramangalargadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpololicramangalargadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpololicramangalargadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpololicramangalargadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpololicramangalargadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpololicramangalargadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDbikerlicradama)
class UDbikerlicradamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDbikerlicradama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDbikerlicradama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDbikerlicradama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDbikerlicradama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDbikerlicradama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDbikerlicradama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDbikerlicradama.objects.all()))- (sum(producto.inversion() for producto in UDbikerlicradama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDbikerlicradama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDbikerlicradama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDbikerlicradama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDbikerlicradama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDbikerlicradama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDfaldashortdama)
class UDfaldashortdamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDfaldashortdama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDfaldashortdama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDfaldashortdama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDfaldashortdama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDfaldashortdama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDfaldashortdama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDfaldashortdama.objects.all()))- (sum(producto.inversion() for producto in UDfaldashortdama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDfaldashortdama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDfaldashortdama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDfaldashortdama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDfaldashortdama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDfaldashortdama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDshortlicradama)
class UDshortlicradamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDshortlicradama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDshortlicradama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDshortlicradama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDshortlicradama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDshortlicradama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDshortlicradama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDshortlicradama.objects.all()))- (sum(producto.inversion() for producto in UDshortlicradama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDshortlicradama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDshortlicradama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDshortlicradama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDshortlicradama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDshortlicradama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDsnikerlicradama)
class UDsnikerlicradamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Marca',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDsnikerlicradama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDsnikerlicradama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDsnikerlicradama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDsnikerlicradama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDsnikerlicradama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDsnikerlicradama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDsnikerlicradama.objects.all()))- (sum(producto.inversion() for producto in UDsnikerlicradama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDsnikerlicradama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDsnikerlicradama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDsnikerlicradama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDsnikerlicradama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDsnikerlicradama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


from .models import UDshortnovadama,UDshorttelamojadadama,UDshortterrydama,UDpoloalgodocamiserodama,UDpoloalgodonmangacortadama,UDpoloalgodonmangalargadama,UDcasacacortavientodama,UDcasacalicradama

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UDshortnovadama)
class UDshortnovadamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDshortnovadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDshortnovadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDshortnovadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDshortnovadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDshortnovadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDshortnovadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDshortnovadama.objects.all()))- (sum(producto.inversion() for producto in UDshortnovadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDshortnovadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDshortnovadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDshortnovadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDshortnovadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDshortnovadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UDshorttelamojadadama)
class UDshorttelamojadadamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDshorttelamojadadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDshorttelamojadadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDshorttelamojadadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDshorttelamojadadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDshorttelamojadadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDshorttelamojadadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDshorttelamojadadama.objects.all()))- (sum(producto.inversion() for producto in UDshorttelamojadadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDshorttelamojadadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDshorttelamojadadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDshorttelamojadadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDshorttelamojadadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDshorttelamojadadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDshortterrydama)
class UDshortterrydamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDshortterrydama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDshortterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDshortterrydama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDshortterrydama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDshortterrydama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDshortterrydama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDshortterrydama.objects.all()))- (sum(producto.inversion() for producto in UDshortterrydama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDshortterrydama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDshortterrydama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDshortterrydama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDshortterrydama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDshortterrydama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpoloalgodocamiserodama)
class UDpoloalgodocamiserodamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpoloalgodocamiserodama.objects.all()))- (sum(producto.inversion() for producto in UDpoloalgodocamiserodama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpoloalgodocamiserodama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpoloalgodonmangacortadama)
class UDpoloalgodonmangacortadamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpoloalgodonmangacortadama.objects.all()))- (sum(producto.inversion() for producto in UDpoloalgodonmangacortadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpoloalgodonmangacortadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################


@admin.register(UDpoloalgodonmangalargadama)
class UDpoloalgodonmangalargadamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDpoloalgodonmangalargadama.objects.all()))- (sum(producto.inversion() for producto in UDpoloalgodonmangalargadama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDpoloalgodonmangalargadama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())





#,UDcasacalicradama

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################

@admin.register(UDcasacacortavientodama)
class UDcasacacortavientodamaaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDcasacacortavientodama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDcasacacortavientodama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDcasacacortavientodama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDcasacacortavientodama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDcasacacortavientodama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDcasacacortavientodama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDcasacacortavientodama.objects.all()))- (sum(producto.inversion() for producto in UDcasacacortavientodama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDcasacacortavientodama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDcasacacortavientodama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDcasacacortavientodama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDcasacacortavientodama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDcasacacortavientodama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDcasacalicradama)
class UDcasacalicradamaaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDcasacalicradama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDcasacalicradama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDcasacalicradama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDcasacalicradama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDcasacalicradama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDcasacalicradama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDcasacalicradama.objects.all()))- (sum(producto.inversion() for producto in UDcasacalicradama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDcasacalicradama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDcasacalicradama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDcasacalicradama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDcasacalicradama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDcasacalicradama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDbivididama)
class UDbivididamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDbivididama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDbivididama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDbivididama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDbivididama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDbivididama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDbivididama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDbivididama.objects.all()))- (sum(producto.inversion() for producto in UDbivididama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDbivididama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDbivididama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDbivididama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDbivididama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDbivididama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())

###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDtopdama)
class UDtopdamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDtopdama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDtopdama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDtopdama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDtopdama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDtopdama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDtopdama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDtopdama.objects.all()))- (sum(producto.inversion() for producto in UDtopdama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDtopdama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDtopdama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDtopdama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDtopdama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDtopdama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())


###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



@admin.register(UDenterizodama)
class UDenterizodamaadmin(admin.ModelAdmin):
    list_display = ('Codigo','Talla','Marca','Modelo','Diseño','Color','Costo','Precio','S1','S2','S3','Almacen','TOTAL','cant_T1','cant_T2','cant_T3','cant_Alm','cant_total','Inversion_Tienda1','Inversion_Tienda2','Inversion_Tienda3','Inversion_Almacen','Inversion','Ganancia','Neto') #SI QUIERO LLAMAR LA FUNCION DE ABAJO TENGO Q COLOCARLE 'total_de_inversion' AQUI AL COSTADO DE INVERSION 
    ordering = ('Color',)
    list_filter=('Talla','Color',)

####################################
    def Inversion(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.inversion() for producto in UDenterizodama.objects.all())
        return total
####################################

    def Inversion_Tienda1(self,request):
        total=sum(producto.inversion_t1() for producto in UDenterizodama.objects.all())
        return total
####################################
    def Inversion_Tienda2(self,request):
        total=sum(producto.inversion_t2() for producto in UDenterizodama.objects.all())
        return total
####################################
    def Inversion_Tienda3(self,request):
        total=sum(producto.inversion_t3() for producto in UDenterizodama.objects.all())
        return total
####################################
    def Inversion_Almacen(self,request):
        total=sum(producto.inversion_almacen() for producto in UDenterizodama.objects.all())
        return total
    
    def Ganancia(self,request):
        # Calcula la suma del resultado de la función 'calcular_valor_total'
        total = sum(producto.ganancia() for producto in UDenterizodama.objects.all())
        return total
####################################
    def Neto(self,request):
        total=(sum(producto.ganancia() for producto in UDenterizodama.objects.all()))- (sum(producto.inversion() for producto in UDenterizodama.objects.all()))
        return total

####################################  
    def cant_total(self,request):
        total = sum(producto.total() for producto in UDenterizodama.objects.all())
        return total
    ####################################
    def cant_T1(self,request):
        total = sum(producto.cant_T1() for producto in UDenterizodama.objects.all())
        return total
    def cant_T2(self,request):
        total = sum(producto.cant_T2() for producto in UDenterizodama.objects.all())
        return total
    def cant_T3(self,request):
        total = sum(producto.cant_T3() for producto in UDenterizodama.objects.all())
        return total
    def cant_Alm(self,request):
        total = sum(producto.cant_alm() for producto in UDenterizodama.objects.all())
        return total
    
########################################
    def TOTAL(self, obj):
        if obj.total() >= 2:
            color = '#56F59C'
        if obj.total() == 1:
            color = 'yellow'
        if obj.total() == 0:
            color = 'red'

        return format_html('<span style="color: {};">{}</span>', color, obj.total())






###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
######################################################################################################################################################
@admin.register(ReportesGenerales)
class ReportesAdmin(admin.ModelAdmin):
    list_display = ('fecha','Total_General','Inventario_general_Tienda_1','Inventario_general_Tienda_2','Inventario_general_Tienda_3','Inventario_general_Almacen',)
 
#
    
    def Inventario_general_Tienda_1(self,obj):
        #suma_general=  sum(producto.inversion_t1() for producto in ConjuntosLomaDama.objects.all()) + sum(producto.inversion_t1() for producto in ConjuntosLicraDama.objects.all()) + sum(producto.inversion_t1() for producto in ConjuntosNovaDama.objects.all()) + sum(producto.inversion_t1() for producto in ConjuntosInterfilDama.objects.all()) + sum(producto.inversion_t1() for producto in ConjuntosFranelaDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosElasticDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosPoliesterDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosPolifreshDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosPlushDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosFranelaPLushDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosTerryDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleDama.objects.all())+ sum(producto.inversion_t1() for producto in ConjuntosBosseDama.objects.all()) + sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosCortavientoVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosElasticVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosFranelaVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosInterfilVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosBosseVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosNovaVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosFranelaPlushVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosPoliesterVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosPolifreshVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaVaron.objects.all()) +sum(producto.inversion_t1() for producto in ConjuntosTerryVaron.objects.all()) 
        suma_general = sum(producto.inversion_t1() for producto in UNOPantalonNiño.objects.all())+sum(producto.inversion_t1() for producto in UVpolooversizedama.objects.all())+sum(producto.inversion_t1() for producto in UVpolooversizevaron.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonpalazodama.objects.all())+sum(producto.inversion_t1() for producto in CNAConjuntoLicraNiña.objects.all())+sum(producto.inversion_t1() for producto in CNAConjuntoNovaNiña.objects.all())+sum(producto.inversion_t1() for producto in CNOConjuntoNovaNiño.objects.all())+sum(producto.inversion_t1() for producto in CNOConjuntoInterfilNiño.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosLicraDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosNovaDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosInterfilDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosFranelaDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosElasticDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosPoliesterDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosPolifreshDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosPlushDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosFranelaPLushDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosTerryDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosBosseDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosLomaDama.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosCortavientoVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosElasticVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosFranelaVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosInterfilVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosBosseVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosNovaVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosFranelaPlushVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosPoliesterVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosPolifreshVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaVaron.objects.all())+sum(producto.inversion_t1() for producto in ConjuntosTerryVaron.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonFranelaBotaRecta.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonInterfilBotaRecta.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonNovaBotaRecta.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonTerryBotaRecta.objects.all())+sum(producto.inversion_t1() for producto in UVPantaloncortavientobotaRecta.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonbossebotaRecta.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonfranelabotajogger.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonterrybotajogger.objects.all())+sum(producto.inversion_t1() for producto in UVBividilicravaron.objects.all())+sum(producto.inversion_t1() for producto in UVcasacascortavientovaron.objects.all())+sum(producto.inversion_t1() for producto in UVPantalonetaslicravaron.objects.all())+sum(producto.inversion_t1() for producto in UVPpoloalgodonvaron.objects.all())+sum(producto.inversion_t1() for producto in UVPpololicravaron.objects.all())+sum(producto.inversion_t1() for producto in UVPpolocompresorvaron.objects.all())+sum(producto.inversion_t1() for producto in UVshortnovavaron.objects.all())+sum(producto.inversion_t1() for producto in UVshorttelamojadavaron.objects.all())+sum(producto.inversion_t1() for producto in UVshortterryvaron.objects.all())+sum(producto.inversion_t1() for producto in UVshortelasticvaron.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonetalicradama.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonnovabotarectadama.objects.all())+sum(producto.inversion_t1() for producto in UDjoggercargodama.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonterrydama.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonfraneladama.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonlicrabotarectadama.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonlomadama.objects.all())+sum(producto.inversion_t1() for producto in UDpantaloninterfildama.objects.all())+sum(producto.inversion_t1() for producto in UDjoggerbotapiefraneladama.objects.all())+sum(producto.inversion_t1() for producto in UDjoggerbotapieterrydama.objects.all())+sum(producto.inversion_t1() for producto in UDjoggerinterfildama.objects.all())+sum(producto.inversion_t1() for producto in UDjoggeroversizefraneladama.objects.all())+sum(producto.inversion_t1() for producto in UDjoggeroversizeterrydama.objects.all())+sum(producto.inversion_t1() for producto in UDpantalonetaterrydama.objects.all())+sum(producto.inversion_t1() for producto in UDpolocroplicradama.objects.all())+sum(producto.inversion_t1() for producto in UDpololicramangacortadama.objects.all())+sum(producto.inversion_t1() for producto in UDpololicramangalargadama.objects.all())+sum(producto.inversion_t1() for producto in UDbikerlicradama.objects.all())+sum(producto.inversion_t1() for producto in UDfaldashortdama.objects.all())+sum(producto.inversion_t1() for producto in UDshortlicradama.objects.all())+sum(producto.inversion_t1() for producto in UDsnikerlicradama.objects.all())+sum(producto.inversion_t1() for producto in UDshortnovadama.objects.all())+sum(producto.inversion_t1() for producto in UDshorttelamojadadama.objects.all())+sum(producto.inversion_t1() for producto in UDshortterrydama.objects.all())+sum(producto.inversion_t1() for producto in UDpoloalgodocamiserodama.objects.all())+sum(producto.inversion_t1() for producto in UDpoloalgodonmangacortadama.objects.all())+sum(producto.inversion_t1() for producto in UDpoloalgodonmangalargadama.objects.all())+sum(producto.inversion_t1() for producto in UDcasacacortavientodama.objects.all())+sum(producto.inversion_t1() for producto in UDcasacalicradama.objects.all())+sum(producto.inversion_t1() for producto in UDbivididama.objects.all())+sum(producto.inversion_t1() for producto in UDtopdama.objects.all())+sum(producto.inversion_t1() for producto in UDenterizodama.objects.all())
        return suma_general
    
    def Inventario_general_Tienda_2(self,obj):
        #suma_general=  sum(producto.inversion_t2() for producto in ConjuntosLomaDama.objects.all()) + sum(producto.inversion_t2() for producto in ConjuntosLicraDama.objects.all()) + sum(producto.inversion_t2() for producto in ConjuntosNovaDama.objects.all()) + sum(producto.inversion_t2() for producto in ConjuntosInterfilDama.objects.all()) + sum(producto.inversion_t2() for producto in ConjuntosFranelaDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosElasticDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosPoliesterDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosTelaMojadaDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosPolifreshDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosPlushDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosFranelaPLushDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosTerryDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosCortavientoReversibleDama.objects.all())+ sum(producto.inversion_t2() for producto in ConjuntosBosseDama.objects.all()) + sum(producto.inversion_t2() for producto in ConjuntosCortavientoReversibleVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosCortavientoVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosElasticVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosFranelaVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosInterfilVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosBosseVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosNovaVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosFranelaPlushVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosPoliesterVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosPolifreshVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosTelaMojadaVaron.objects.all()) +sum(producto.inversion_t2() for producto in ConjuntosTerryVaron.objects.all()) 
        suma_general = sum(producto.inversion_t2() for producto in UNOPantalonNiño.objects.all())+sum(producto.inversion_t2() for producto in UVpolooversizedama.objects.all())+sum(producto.inversion_t2() for producto in UVpolooversizevaron.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonpalazodama.objects.all())+sum(producto.inversion_t2() for producto in CNAConjuntoLicraNiña.objects.all())+sum(producto.inversion_t2() for producto in CNAConjuntoNovaNiña.objects.all())+sum(producto.inversion_t2() for producto in CNOConjuntoNovaNiño.objects.all())+sum(producto.inversion_t2() for producto in CNOConjuntoInterfilNiño.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosLicraDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosNovaDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosInterfilDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosFranelaDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosElasticDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosPoliesterDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosTelaMojadaDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosPolifreshDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosPlushDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosFranelaPLushDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosTerryDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosCortavientoReversibleDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosBosseDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosLomaDama.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosCortavientoReversibleVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosCortavientoVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosElasticVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosFranelaVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosInterfilVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosBosseVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosNovaVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosFranelaPlushVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosPoliesterVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosPolifreshVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosTelaMojadaVaron.objects.all())+sum(producto.inversion_t2() for producto in ConjuntosTerryVaron.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonFranelaBotaRecta.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonInterfilBotaRecta.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonNovaBotaRecta.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonTerryBotaRecta.objects.all())+sum(producto.inversion_t2() for producto in UVPantaloncortavientobotaRecta.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonbossebotaRecta.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonfranelabotajogger.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonterrybotajogger.objects.all())+sum(producto.inversion_t2() for producto in UVBividilicravaron.objects.all())+sum(producto.inversion_t2() for producto in UVcasacascortavientovaron.objects.all())+sum(producto.inversion_t2() for producto in UVPantalonetaslicravaron.objects.all())+sum(producto.inversion_t2() for producto in UVPpoloalgodonvaron.objects.all())+sum(producto.inversion_t2() for producto in UVPpololicravaron.objects.all())+sum(producto.inversion_t2() for producto in UVPpolocompresorvaron.objects.all())+sum(producto.inversion_t2() for producto in UVshortnovavaron.objects.all())+sum(producto.inversion_t2() for producto in UVshorttelamojadavaron.objects.all())+sum(producto.inversion_t2() for producto in UVshortterryvaron.objects.all())+sum(producto.inversion_t2() for producto in UVshortelasticvaron.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonetalicradama.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonnovabotarectadama.objects.all())+sum(producto.inversion_t2() for producto in UDjoggercargodama.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonterrydama.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonfraneladama.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonlicrabotarectadama.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonlomadama.objects.all())+sum(producto.inversion_t2() for producto in UDpantaloninterfildama.objects.all())+sum(producto.inversion_t2() for producto in UDjoggerbotapiefraneladama.objects.all())+sum(producto.inversion_t2() for producto in UDjoggerbotapieterrydama.objects.all())+sum(producto.inversion_t2() for producto in UDjoggerinterfildama.objects.all())+sum(producto.inversion_t2() for producto in UDjoggeroversizefraneladama.objects.all())+sum(producto.inversion_t2() for producto in UDjoggeroversizeterrydama.objects.all())+sum(producto.inversion_t2() for producto in UDpantalonetaterrydama.objects.all())+sum(producto.inversion_t2() for producto in UDpolocroplicradama.objects.all())+sum(producto.inversion_t2() for producto in UDpololicramangacortadama.objects.all())+sum(producto.inversion_t2() for producto in UDpololicramangalargadama.objects.all())+sum(producto.inversion_t2() for producto in UDbikerlicradama.objects.all())+sum(producto.inversion_t2() for producto in UDfaldashortdama.objects.all())+sum(producto.inversion_t2() for producto in UDshortlicradama.objects.all())+sum(producto.inversion_t2() for producto in UDsnikerlicradama.objects.all())+sum(producto.inversion_t2() for producto in UDshortnovadama.objects.all())+sum(producto.inversion_t2() for producto in UDshorttelamojadadama.objects.all())+sum(producto.inversion_t2() for producto in UDshortterrydama.objects.all())+sum(producto.inversion_t2() for producto in UDpoloalgodocamiserodama.objects.all())+sum(producto.inversion_t2() for producto in UDpoloalgodonmangacortadama.objects.all())+sum(producto.inversion_t2() for producto in UDpoloalgodonmangalargadama.objects.all())+sum(producto.inversion_t2() for producto in UDcasacacortavientodama.objects.all())+sum(producto.inversion_t2() for producto in UDcasacalicradama.objects.all())+sum(producto.inversion_t2() for producto in UDbivididama.objects.all())+sum(producto.inversion_t2() for producto in UDtopdama.objects.all())+sum(producto.inversion_t2() for producto in UDenterizodama.objects.all())
        return suma_general

    def Inventario_general_Tienda_3(self,obj):
        #suma_general=  sum(producto.inversion_t3() for producto in ConjuntosLomaDama.objects.all()) + sum(producto.inversion_t3() for producto in ConjuntosLicraDama.objects.all()) + sum(producto.inversion_t3() for producto in ConjuntosNovaDama.objects.all()) + sum(producto.inversion_t3() for producto in ConjuntosInterfilDama.objects.all()) + sum(producto.inversion_t3() for producto in ConjuntosFranelaDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosElasticDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosPoliesterDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosTelaMojadaDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosPolifreshDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosPlushDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosFranelaPLushDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosTerryDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosCortavientoReversibleDama.objects.all())+ sum(producto.inversion_t3() for producto in ConjuntosBosseDama.objects.all()) + sum(producto.inversion_t3() for producto in ConjuntosCortavientoReversibleVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosCortavientoVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosElasticVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosFranelaVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosInterfilVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosBosseVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosNovaVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosFranelaPlushVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosPoliesterVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosPolifreshVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosTelaMojadaVaron.objects.all()) +sum(producto.inversion_t3() for producto in ConjuntosTerryVaron.objects.all()) 
        suma_general = sum(producto.inversion_t3() for producto in UNOPantalonNiño.objects.all())+sum(producto.inversion_t3() for producto in UVpolooversizedama.objects.all())+sum(producto.inversion_t3() for producto in UVpolooversizevaron.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonpalazodama.objects.all())+sum(producto.inversion_t3() for producto in CNAConjuntoLicraNiña.objects.all())+sum(producto.inversion_t3() for producto in CNAConjuntoNovaNiña.objects.all())+sum(producto.inversion_t3() for producto in CNOConjuntoNovaNiño.objects.all())+sum(producto.inversion_t3() for producto in CNOConjuntoInterfilNiño.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosLicraDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosNovaDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosInterfilDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosFranelaDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosElasticDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosPoliesterDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosTelaMojadaDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosPolifreshDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosPlushDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosFranelaPLushDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosTerryDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosCortavientoReversibleDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosBosseDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosLomaDama.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosCortavientoReversibleVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosCortavientoVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosElasticVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosFranelaVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosInterfilVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosBosseVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosNovaVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosFranelaPlushVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosPoliesterVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosPolifreshVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosTelaMojadaVaron.objects.all())+sum(producto.inversion_t3() for producto in ConjuntosTerryVaron.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonFranelaBotaRecta.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonInterfilBotaRecta.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonNovaBotaRecta.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonTerryBotaRecta.objects.all())+sum(producto.inversion_t3() for producto in UVPantaloncortavientobotaRecta.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonbossebotaRecta.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonfranelabotajogger.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonterrybotajogger.objects.all())+sum(producto.inversion_t3() for producto in UVBividilicravaron.objects.all())+sum(producto.inversion_t3() for producto in UVcasacascortavientovaron.objects.all())+sum(producto.inversion_t3() for producto in UVPantalonetaslicravaron.objects.all())+sum(producto.inversion_t3() for producto in UVPpoloalgodonvaron.objects.all())+sum(producto.inversion_t3() for producto in UVPpololicravaron.objects.all())+sum(producto.inversion_t3() for producto in UVPpolocompresorvaron.objects.all())+sum(producto.inversion_t3() for producto in UVshortnovavaron.objects.all())+sum(producto.inversion_t3() for producto in UVshorttelamojadavaron.objects.all())+sum(producto.inversion_t3() for producto in UVshortterryvaron.objects.all())+sum(producto.inversion_t3() for producto in UVshortelasticvaron.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonetalicradama.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonnovabotarectadama.objects.all())+sum(producto.inversion_t3() for producto in UDjoggercargodama.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonterrydama.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonfraneladama.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonlicrabotarectadama.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonlomadama.objects.all())+sum(producto.inversion_t3() for producto in UDpantaloninterfildama.objects.all())+sum(producto.inversion_t3() for producto in UDjoggerbotapiefraneladama.objects.all())+sum(producto.inversion_t3() for producto in UDjoggerbotapieterrydama.objects.all())+sum(producto.inversion_t3() for producto in UDjoggerinterfildama.objects.all())+sum(producto.inversion_t3() for producto in UDjoggeroversizefraneladama.objects.all())+sum(producto.inversion_t3() for producto in UDjoggeroversizeterrydama.objects.all())+sum(producto.inversion_t3() for producto in UDpantalonetaterrydama.objects.all())+sum(producto.inversion_t3() for producto in UDpolocroplicradama.objects.all())+sum(producto.inversion_t3() for producto in UDpololicramangacortadama.objects.all())+sum(producto.inversion_t3() for producto in UDpololicramangalargadama.objects.all())+sum(producto.inversion_t3() for producto in UDbikerlicradama.objects.all())+sum(producto.inversion_t3() for producto in UDfaldashortdama.objects.all())+sum(producto.inversion_t3() for producto in UDshortlicradama.objects.all())+sum(producto.inversion_t3() for producto in UDsnikerlicradama.objects.all())+sum(producto.inversion_t3() for producto in UDshortnovadama.objects.all())+sum(producto.inversion_t3() for producto in UDshorttelamojadadama.objects.all())+sum(producto.inversion_t3() for producto in UDshortterrydama.objects.all())+sum(producto.inversion_t3() for producto in UDpoloalgodocamiserodama.objects.all())+sum(producto.inversion_t3() for producto in UDpoloalgodonmangacortadama.objects.all())+sum(producto.inversion_t3() for producto in UDpoloalgodonmangalargadama.objects.all())+sum(producto.inversion_t3() for producto in UDcasacacortavientodama.objects.all())+sum(producto.inversion_t3() for producto in UDcasacalicradama.objects.all())+sum(producto.inversion_t3() for producto in UDbivididama.objects.all())+sum(producto.inversion_t3() for producto in UDtopdama.objects.all())+sum(producto.inversion_t3() for producto in UDenterizodama.objects.all())
        return suma_general

    def Inventario_general_Almacen(self,obj):
        #suma_general=  sum(producto.inversion_almacen() for producto in ConjuntosLomaDama.objects.all()) + sum(producto.inversion_almacen() for producto in ConjuntosLicraDama.objects.all()) + sum(producto.inversion_almacen() for producto in ConjuntosNovaDama.objects.all()) + sum(producto.inversion_almacen() for producto in ConjuntosInterfilDama.objects.all()) + sum(producto.inversion_almacen() for producto in ConjuntosFranelaDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosElasticDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosPoliesterDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosTelaMojadaDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosPolifreshDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosPlushDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosFranelaPLushDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosTerryDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosCortavientoReversibleDama.objects.all())+ sum(producto.inversion_almacen() for producto in ConjuntosBosseDama.objects.all()) + sum(producto.inversion_almacen() for producto in ConjuntosCortavientoReversibleVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosCortavientoVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosElasticVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosFranelaVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosInterfilVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosBosseVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosNovaVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosFranelaPlushVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosPoliesterVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosPolifreshVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosTelaMojadaVaron.objects.all()) +sum(producto.inversion_almacen() for producto in ConjuntosTerryVaron.objects.all()) 
        suma_general = sum(producto.inversion_almacen() for producto in UNOPantalonNiño.objects.all())+sum(producto.inversion_almacen() for producto in UVpolooversizedama.objects.all())+sum(producto.inversion_almacen() for producto in UVpolooversizevaron.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonpalazodama.objects.all())+sum(producto.inversion_almacen() for producto in CNAConjuntoLicraNiña.objects.all())+sum(producto.inversion_almacen() for producto in CNAConjuntoNovaNiña.objects.all())+sum(producto.inversion_almacen() for producto in CNOConjuntoNovaNiño.objects.all())+sum(producto.inversion_almacen() for producto in CNOConjuntoInterfilNiño.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosLicraDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosNovaDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosInterfilDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosFranelaDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosElasticDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosPoliesterDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosTelaMojadaDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosPolifreshDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosPlushDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosFranelaPLushDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosTerryDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosCortavientoReversibleDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosBosseDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosLomaDama.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosCortavientoReversibleVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosCortavientoVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosElasticVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosFranelaVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosInterfilVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosBosseVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosNovaVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosFranelaPlushVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosPoliesterVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosPolifreshVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosTelaMojadaVaron.objects.all())+sum(producto.inversion_almacen() for producto in ConjuntosTerryVaron.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonFranelaBotaRecta.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonInterfilBotaRecta.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonNovaBotaRecta.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonTerryBotaRecta.objects.all())+sum(producto.inversion_almacen() for producto in UVPantaloncortavientobotaRecta.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonbossebotaRecta.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonfranelabotajogger.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonterrybotajogger.objects.all())+sum(producto.inversion_almacen() for producto in UVBividilicravaron.objects.all())+sum(producto.inversion_almacen() for producto in UVcasacascortavientovaron.objects.all())+sum(producto.inversion_almacen() for producto in UVPantalonetaslicravaron.objects.all())+sum(producto.inversion_almacen() for producto in UVPpoloalgodonvaron.objects.all())+sum(producto.inversion_almacen() for producto in UVPpololicravaron.objects.all())+sum(producto.inversion_almacen() for producto in UVPpolocompresorvaron.objects.all())+sum(producto.inversion_almacen() for producto in UVshortnovavaron.objects.all())+sum(producto.inversion_almacen() for producto in UVshorttelamojadavaron.objects.all())+sum(producto.inversion_almacen() for producto in UVshortterryvaron.objects.all())+sum(producto.inversion_almacen() for producto in UVshortelasticvaron.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonetalicradama.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonnovabotarectadama.objects.all())+sum(producto.inversion_almacen() for producto in UDjoggercargodama.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonterrydama.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonfraneladama.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonlicrabotarectadama.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonlomadama.objects.all())+sum(producto.inversion_almacen() for producto in UDpantaloninterfildama.objects.all())+sum(producto.inversion_almacen() for producto in UDjoggerbotapiefraneladama.objects.all())+sum(producto.inversion_almacen() for producto in UDjoggerbotapieterrydama.objects.all())+sum(producto.inversion_almacen() for producto in UDjoggerinterfildama.objects.all())+sum(producto.inversion_almacen() for producto in UDjoggeroversizefraneladama.objects.all())+sum(producto.inversion_almacen() for producto in UDjoggeroversizeterrydama.objects.all())+sum(producto.inversion_almacen() for producto in UDpantalonetaterrydama.objects.all())+sum(producto.inversion_almacen() for producto in UDpolocroplicradama.objects.all())+sum(producto.inversion_almacen() for producto in UDpololicramangacortadama.objects.all())+sum(producto.inversion_almacen() for producto in UDpololicramangalargadama.objects.all())+sum(producto.inversion_almacen() for producto in UDbikerlicradama.objects.all())+sum(producto.inversion_almacen() for producto in UDfaldashortdama.objects.all())+sum(producto.inversion_almacen() for producto in UDshortlicradama.objects.all())+sum(producto.inversion_almacen() for producto in UDsnikerlicradama.objects.all())+sum(producto.inversion_almacen() for producto in UDshortnovadama.objects.all())+sum(producto.inversion_almacen() for producto in UDshorttelamojadadama.objects.all())+sum(producto.inversion_almacen() for producto in UDshortterrydama.objects.all())+sum(producto.inversion_almacen() for producto in UDpoloalgodocamiserodama.objects.all())+sum(producto.inversion_almacen() for producto in UDpoloalgodonmangacortadama.objects.all())+sum(producto.inversion_almacen() for producto in UDpoloalgodonmangalargadama.objects.all())+sum(producto.inversion_almacen() for producto in UDcasacacortavientodama.objects.all())+sum(producto.inversion_almacen() for producto in UDcasacalicradama.objects.all())+sum(producto.inversion_almacen() for producto in UDbivididama.objects.all())+sum(producto.inversion_almacen() for producto in UDtopdama.objects.all())+sum(producto.inversion_almacen() for producto in UDenterizodama.objects.all())          
        return suma_general

    def Total_General(self, obj):
        inventario_tienda_1 = self.Inventario_general_Tienda_1(obj)
        inventario_tienda_2 = self.Inventario_general_Tienda_2(obj)
        inventario_tienda_3 = self.Inventario_general_Tienda_3(obj)
        inventario_almacen = self.Inventario_general_Almacen(obj)
        total = inventario_tienda_1+inventario_tienda_2+inventario_tienda_3 + inventario_almacen
        return total
    

@admin.register(InventariodeTotales)
class InventariodeTotalesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'Totales')

    def Totales(self, obj):
        enterizos = sum(producto.cant_T1() for producto in UDenterizodama.objects.all())
        tops = sum(producto.cant_T1() for producto in UDtopdama.objects.all())

        return format_html(
            'Enterizos T1: {}<br>Top Dama T1: {}',
            enterizos, tops
        )

    Totales.short_description = "Totales por Producto"




#sum(producto.inversion_t1() for producto in ConjuntosLicraDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosNovaDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosInterfilDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosFranelaDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosElasticDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosPoliesterDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosPolifreshDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosPlushDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosFranelaPLushDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosTerryDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosBosseDama.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosLomaDama.objects.all())+

#sum(producto.inversion_t1() for producto in ConjuntosCortavientoReversibleVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosCortavientoVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosElasticVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosFranelaVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosInterfilVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosBosseVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosNovaVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosFranelaPlushVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosPoliesterVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosPolifreshVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosTelaMojadaVaron.objects.all())+
#sum(producto.inversion_t1() for producto in ConjuntosTerryVaron.objects.all())+


#sum(producto.inversion_t1() for producto in UVPantalonFranelaBotaRecta.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantalonInterfilBotaRecta.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantalonNovaBotaRecta.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantalonTerryBotaRecta.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantaloncortavientobotaRecta.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantalonbossebotaRecta.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantalonfranelabotajogger.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantalonterrybotajogger.objects.all())+
#sum(producto.inversion_t1() for producto in UVBividilicravaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVcasacascortavientovaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVPantalonetaslicravaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVPpoloalgodonvaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVPpololicravaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVPpolocompresorvaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVshortnovavaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVshorttelamojadavaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVshortterryvaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVshortelasticvaron.objects.all())+
#sum(producto.inversion_t1() for producto in UVpolooversizevaron.objects.all())+


#sum(producto.inversion_t1() for producto in UDpantalonetalicradama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantalonnovabotarectadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDjoggercargodama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantalonterrydama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantalonfraneladama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantalonlicrabotarectadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantalonlomadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantaloninterfildama.objects.all())+
#sum(producto.inversion_t1() for producto in UDjoggerbotapiefraneladama.objects.all())+
#sum(producto.inversion_t1() for producto in UDjoggerbotapieterrydama.objects.all())+
#sum(producto.inversion_t1() for producto in UDjoggerinterfildama.objects.all())+
#sum(producto.inversion_t1() for producto in UDjoggeroversizefraneladama.objects.all())+
#sum(producto.inversion_t1() for producto in UDjoggeroversizeterrydama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantalonetaterrydama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpolocroplicradama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpololicramangacortadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpololicramangalargadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDbikerlicradama.objects.all())+
#sum(producto.inversion_t1() for producto in UDfaldashortdama.objects.all())+
#sum(producto.inversion_t1() for producto in UDshortlicradama.objects.all())+
#sum(producto.inversion_t1() for producto in UDsnikerlicradama.objects.all())+
#sum(producto.inversion_t1() for producto in UDshortnovadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDshorttelamojadadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDshortterrydama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpoloalgodocamiserodama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpoloalgodonmangacortadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpoloalgodonmangalargadama.objects.all())+
#sum(producto.inversion_t1() for producto in UDcasacacortavientodama.objects.all())+
#sum(producto.inversion_t1() for producto in UDcasacalicradama.objects.all())+
#sum(producto.inversion_t1() for producto in UDbivididama.objects.all())+
#sum(producto.inversion_t1() for producto in UDtopdama.objects.all())+
#sum(producto.inversion_t1() for producto in UDenterizodama.objects.all())+
#sum(producto.inversion_t1() for producto in UDpantalonpalazodama.objects.all())+
#sum(producto.inversion_t1() for producto in UVpolooversizedama.objects.all())+




#sum(producto.inversion_t1() for producto in CNOConjuntoInterfilNiño.objects.all())+
#sum(producto.inversion_t1() for producto in CNOConjuntoNovaNiño.objects.all())+

#sum(producto.inversion_t1() for producto in CNAConjuntoNovaNiña.objects.all())+
#sum(producto.inversion_t1() for producto in CNAConjuntoLicraNiña.objects.all())+


#CNAConjuntoNovaNiña

#sum(producto.inversion_t1() for producto in UDbivididama.objects.all())+sum(producto.inversion_t1() for producto in UDtopdama.objects.all())+sum(producto.inversion_t1() for producto in UDenterizodama.objects.all())+