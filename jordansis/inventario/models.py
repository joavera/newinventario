from django.db import models

# Create your models here.
# gruponombre=models.CharField(max_length=150)


class grupo(models.Model):

    grupoanulado=models.CharField(max_length=1)
    gruponombre=models.CharField(max_length=150)
    Estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    grupoanulado = models.CharField(max_length=1, choices=Estado, help_text="Seleccione el Estado", default='1')
    def __str__(self):
        return  self.gruponombre


class productos(models.Model):
    productosnombre = models.CharField(max_length=150)
    productospreciovta = models.FloatField()
    productoscodigo = models.CharField(max_length=50)
    productosexistencia = models.IntegerField()
    productosgrupo = models.ForeignKey(grupo, on_delete=models.CASCADE)
    Estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    productosanulado = models.CharField(max_length=1, choices=Estado, help_text="Seleccione el Estado", default='1')

    def __str__(self):
        return self.productosgrupo

class proveedor(models.Model):
    proveedorcedula=models.CharField(max_length=13)
    proveedornombres=models.CharField(max_length=150)
    proveedortelefono=models.CharField(max_length=50)
    Estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    proveedoranulado= models.CharField(max_length=1, choices=Estado, help_text="Seleccione el Estado", default='1')
    def __str__(self):
        return  self.proveedornombres

class clientes(models.Model):
    clientecedula=models.CharField(max_length=13)
    clientetelefono=models.CharField(max_length=50)
    clientenombre=models.CharField(max_length=150)
    Estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    clienteanulado = models.CharField(max_length=1, choices=Estado, help_text="Seleccione el Estado", default='1')

    def __str__(self):
        return self.clientenombre

class comprastien(models.Model):
    comprastienfechacompras=models.DateField(null=True,blank=True)
    comprastienobservacion=models.CharField(max_length=150)
    comprasnofactura=models.CharField(max_length=50)
    comprastienfechafactura=models.DateField()
    comprastiensubtotal =models.FloatField(default=0)
    comprastiendescuento=models.FloatField(default=0)
    comprastientotal=models.FloatField(default=0)
    comprastienproveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)

class comprasdetalles(models.Model):
   comprasdetallecomprastienda=models.ForeignKey(comprastien,on_delete=models.CASCADE)
   comprasdetalleproductos=models.ForeignKey(productos,on_delete=models.CASCADE)
   comprasdetallecantidad=models.IntegerField()
   comprasdetalleprecio=models.FloatField()
   comprasdetallesubtotal=models.FloatField()
   comprasdetalledescuento=models.FloatField()
   comprasdetalletotal=models.FloatField

class ventatienda(models.Model):
    ventatiendaclientes = models.ForeignKey(clientes, on_delete=models.CASCADE)
    ventastiendafechaventa=models.DateField(null=True,blank=True)
    ventatiendaobservacion=models.CharField(max_length=150)
    ventanofactura=models.CharField(max_length=50)
    ventatiendafechafactura=models.DateField()
    ventatiendacsubtotal =models.FloatField(default=0)
    ventatiendacdescuento=models.FloatField(default=0)
    ventatiendatotal=models.FloatField(default=0)


class ventadetalle(models.Model):
   ventadetalleventatienda=models.ForeignKey(ventatienda,on_delete=models.CASCADE)
   ventadetalleproductos=models.ForeignKey(productos,on_delete=models.CASCADE)
   ventadetallecantidad=models.IntegerField()
   ventadetalleprecio=models.FloatField()
   ventadetallesubtotal=models.FloatField()
   ventadetalledescuento=models.FloatField()
   ventadetalletotal=models.FloatField

class materia(models.Model):
    materianombre = models.CharField(max_length=150)

class estudiante(models.Model):
    estudiantenombre = models.CharField(max_length=150)
    estudianteapellido = models.CharField(max_length=150)

class notas(models.Model):
    ventadetalleventatienda = models.ForeignKey(materia, on_delete=models.CASCADE)
    ventadetalleproductos = models.ForeignKey(estudiante, on_delete=models.CASCADE)
    notaestudiante = models.CharField(max_length=150)

