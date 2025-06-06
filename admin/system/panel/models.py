from django.db import models
from django.utils import timezone

# Create your models here.

class Tareas(models.Model):
    id = models.IntegerField(primary_key=True)
    tienda =models.CharField(max_length=20, null=False)
    descripcion =models.CharField(max_length=20, null=False)
    f_registro = models.DateTimeField(auto_now_add=True,null=True)
    realizado = models.CharField(max_length=2, null=False)

    def __str__(self):
        texto="{0}{1}{2}{3}{4}"
        return texto.format(self.id,self.tienda,self.descripcion,self.f_registro,self.realizado)
    
    class Meta:
        verbose_name_plural = 'Tareas Diarias'


class Cliente(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosLicraDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Licra '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosNovaDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Nova '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosInterfilDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Interfil '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosFranelaDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Franela '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosElasticDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Elastic '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosPlushDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Plush '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosPoliesterDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Poliester '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosTelaMojadaDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Tela Mojada '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosPolifreshDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Poli Fresh '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosCortavientoReversibleDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Cortaviento Reversible '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosTerryDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . French Terry '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosFranelaPLushDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Franela / Plush '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosBosseDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Bosse '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen




###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosLomaDama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CD . Loma '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen





###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class ConjuntosCortavientoReversibleVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Cortaviento Reversible '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosCortavientoVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Cortaviento  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosElasticVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Elastic  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosFranelaVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Franela  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosInterfilVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Interfil  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosBosseVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Bosse  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosNovaVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Nova  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosFranelaPlushVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Franela / Plush  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosPoliesterVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Poliester  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosPolifreshVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Poli Fresh  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosTelaMojadaVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Tela Mojada  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen





###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class ConjuntosTerryVaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CV . Terry  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonFranelaBotaRecta(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Pantalon Franela Bota Recta  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen





###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonTerryBotaRecta(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Pantalon Terry Bota Recta  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonNovaBotaRecta(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Pantalon Nova Bota Recta  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonInterfilBotaRecta(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Pantalon Interfil Bota Recta  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen





###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantaloncortavientobotaRecta(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Pantalon Cortaviento Bota Recta  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonbossebotaRecta(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Pantalon Bosse Bota Recta  '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonterrybotajogger(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Jogger Terry   '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen





###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonfranelabotajogger(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Jogger Franela   '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPantalonetaslicravaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Pantalonetas licra   '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVBividilicravaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Bividi licra   '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVcasacascortavientovaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Casacas cortaviento    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPpoloalgodonvaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Polo Algodon    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPpololicravaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Polo Licra    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVPpolocompresorvaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Polo Compresor    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVshortnovavaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Short Nova    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVshortelasticvaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Short Elastic    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVshortterryvaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Short Terry    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVshorttelamojadavaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Short Tela Mojada    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVpolooversizevaron(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UV . Polos Oversize     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UVpolooversizedama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Polos Oversize     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


class UDpantalonnovabotarectadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantalon Nova Bota Recta    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen






###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantalonetalicradama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantaloneta Licra    '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDjoggercargodama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Jogger Cargo     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantalonlomadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantalon Loma Bota Recta     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen







###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantaloninterfildama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantalon Interfil Bota Recta     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantalonterrydama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantalon Terry Bota Recta     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantalonlicrabotarectadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantalon Licra Bota Recta     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantalonfraneladama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantalon Franela Bota Recta '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantalonetaterrydama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantaloneta Terry Pitillo '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDjoggerinterfildama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Jogger Interfil     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDjoggeroversizeterrydama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Jogger Oversize Terry     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDjoggerbotapieterrydama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Jogger Botapie Terry     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDjoggeroversizefraneladama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Jogger Oversize Franela     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDjoggerbotapiefraneladama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Jogger Botapie Franela     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpololicramangacortadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Polo Licra Manga Corta     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen




###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpololicramangalargadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Polo Licra Manga Larga     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpolocroplicradama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Polo Crop Licra     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDsnikerlicradama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Sniker Licra     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDbikerlicradama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Biker Licra     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDshortlicradama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Short Licra     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen




###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDfaldashortdama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Falda Short Licra     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDshortterrydama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Short Terry     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDshorttelamojadadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Short Tela Mojada     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDshortnovadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Short Nova     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpoloalgodonmangacortadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Polo Algodon Manga Corta     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpoloalgodonmangalargadama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Polo Algodon Manga Larga     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpoloalgodocamiserodama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Polo Algodon Cuello Camisero     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDcasacalicradama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Casaca Licra     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDcasacacortavientodama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Casaca Cortaviento     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    
###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDbivididama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Bividi      '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    
###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDtopdama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Top     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
    


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDenterizodama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Enterizo     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen
###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UDpantalonpalazodama(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UD . Pantalon Palazo      '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen



###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class CNOConjuntoNovaNiño(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CNO . Conjunto Nova Niño     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class CNOConjuntoInterfilNiño(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CNO . Conjunto Interfil Niño     '
    
    def total(self):
        a = self.S1 + self.S2 + self.S3 + self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class UNOPantalonNiño(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'UNO . Pantalon  Niño     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen













###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class CNAConjuntoNovaNiña(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CNA . Conjunto Nova Niña     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen




###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


class CNAConjuntoLicraNiña(models.Model):
    Codigo=models.CharField(primary_key=True,max_length=100,null=False)
    Talla=models.CharField(max_length=100,null=False)
    Marca=models.CharField(max_length=100,null=False)
    Modelo=models.CharField(max_length=100,null=False)
    Diseño=models.CharField(max_length=100,null=False)
    Color=models.CharField(max_length=100,null=False)
    Costo=models.IntegerField(default=18)
    Precio=models.IntegerField()
    S1=models.IntegerField(default=0)
    S2=models.IntegerField(default=0)
    S3=models.IntegerField(default=0)
    Almacen=models.IntegerField(default=0)
    Global=models.IntegerField(default=0)
    def __str__(self):
        texto="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}"
        return texto.format(self.Codigo,self.Talla,self.Marca,self.Modelo,self.Diseño,self.Color,self.Costo,self.Precio,self.S1,self.S2,self.S3,self.Almacen,self.Global)
    
    class Meta:
        verbose_name_plural = 'CNA . Conjunto Licra Niña     '
    
    def total(self):
        a =self.S1 + self.S2 + self.S3 +self.Almacen
        return a
    
    def inversion(self):
        a=self.total()
        return self.Costo*a
##################################################################################################################
    def inversion_t1(self):
        return self.Costo*self.S1
    
    def inversion_t2(self):
        return self.Costo*self.S2

    def inversion_t3(self):
        return self.Costo*self.S3

    def inversion_almacen(self):
        return self.Costo*self.Almacen
##################################################################################################################     
    def ganancia(self):
        b=self.total()
        return self.Precio*b
    
    def cant_T1(self):
        return self.S1
    
    def cant_T2(self):
        return self.S2
    
    def cant_T3(self):
        return self.S3
    
    def cant_alm(self):
        return self.Almacen

















###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


from django.db import models
from django.utils import timezone

class Venta(models.Model):
    TICKET_PREFIX = '0'  # Define el prefijo inicial para el número de ticket

    numero_ticket = models.CharField(max_length=12, unique=True, editable=False)  # Número de ticket único
    descripcion = models.TextField()  # Descripción sin límite de texto
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para almacenar números con dos decimales
    METODO_PAGO_CHOICES = [
        ('E', 'Efectivo'),
        ('Y', 'Yape'),
        ('T', 'Tarjeta'),
    ]
    metodo_pago = models.CharField(max_length=1, choices=METODO_PAGO_CHOICES, default='E')  # Tres opciones de método de pago con valor predeterminado
    fecha = models.DateTimeField(default=timezone.now)  # Fecha y hora actual por defecto
    ESTADO_CHOICES = [
        ('R', 'Revisado'),
        ('N', 'No Revisado'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='N')  # Opciones de estado con valor predeterminado

    def save(self, *args, **kwargs):
        if not self.id:
            last_venta = Venta.objects.all().order_by('id').last()
            if last_venta:
                last_ticket_number = int(last_venta.numero_ticket[len(self.TICKET_PREFIX):])
                self.numero_ticket = self.TICKET_PREFIX + str(last_ticket_number + 1).zfill(8)
            else:
                self.numero_ticket = self.TICKET_PREFIX + '1'.zfill(9)
        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f'Ticket {self.numero_ticket}'


    class Meta:
        verbose_name_plural = ' ADMIN. TICKETS DE VENTA TIENDA 1'

###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################

class Venta2(models.Model):
    TICKET_PREFIX = '0'  # Define el prefijo inicial para el número de ticket

    numero_ticket = models.CharField(max_length=12, unique=True, editable=False)  # Número de ticket único
    descripcion = models.TextField()  # Descripción sin límite de texto
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para almacenar números con dos decimales
    METODO_PAGO_CHOICES = [
        ('E', 'Efectivo'),
        ('Y', 'Yape'),
        ('T', 'Tarjeta'),
    ]
    metodo_pago = models.CharField(max_length=1, choices=METODO_PAGO_CHOICES, default='E')  # Tres opciones de método de pago con valor predeterminado
    fecha = models.DateTimeField(default=timezone.now)  # Fecha y hora actual por defecto
    ESTADO_CHOICES = [
        ('R', 'Revisado'),
        ('N', 'No Revisado'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='N')  # Opciones de estado con valor predeterminado

    def save(self, *args, **kwargs):
        if not self.id:
            last_venta = Venta2.objects.all().order_by('id').last()
            if last_venta:
                last_ticket_number = int(last_venta.numero_ticket[len(self.TICKET_PREFIX):])
                self.numero_ticket = self.TICKET_PREFIX + str(last_ticket_number + 1).zfill(8)
            else:
                self.numero_ticket = self.TICKET_PREFIX + '1'.zfill(9)
        super(Venta2, self).save(*args, **kwargs)

    def __str__(self):
        return f'Ticket {self.numero_ticket}'


    class Meta:
        verbose_name_plural = ' ADMIN. TICKETS DE VENTA TIENDA 2'








###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################





class Ventas_Mensuale(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Fecha: {self.fecha}, Monto: {self.monto}"

    class Meta:
        verbose_name_plural = ' ADMIN . INGRESO TOTAL DIARIO TIENDA 1'


class Ventas_Mensuale2(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Fecha: {self.fecha}, Monto: {self.monto}"

    class Meta:
        verbose_name_plural = ' ADMIN . INGRESO TOTAL DIARIO TIENDA 2'

###################################################################################################################



class ReportesGenerales(models.Model):
    fecha = models.CharField(primary_key=True,max_length=100,null=False)

    class Meta:
        #db_table = 'Reportes Generales'
        verbose_name_plural = 'ADMIN . REPORTE GENERAL'


###################################################################################################################



class InventariodeTotales(models.Model):
    fecha = models.CharField(primary_key=True,max_length=100,null=False)

    class Meta:
        #db_table = 'Reportes Generales'
        verbose_name_plural = 'ADMIN . REPORTE DE INVENTARIOS TOTAL'


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

class TiendaArchivo(models.Model):
    archivo = models.FileField(upload_to='archivos_excel/')
    tienda1 = models.IntegerField()
    tienda2 = models.IntegerField()

    def __str__(self):
        return f"Tienda1: {self.tienda1}, Tienda2: {self.tienda2}"
    

    class Meta:
        #db_table = 'Reportes Generales'
        verbose_name_plural = 'ADMIN . DATOS ESTADÍSTICOS MENSUALES'


    def Ganancia_Tienda1(self):
        return round(self.tienda1 * 0.6)

    def Ganancia_Tienda2(self):
        return round(self.tienda2 * 0.6)

    def Ganancia_Total(self):
        return self.Ganancia_Tienda1() + self.Ganancia_Tienda2()

###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################


###################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

