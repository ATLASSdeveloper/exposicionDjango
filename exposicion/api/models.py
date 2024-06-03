from django.db import models

class Bodega(models.Model):
    bod_id = models.AutoField(primary_key=True)
    bod_nombre = models.CharField(max_length=30)
    bod_ubicacion = models.CharField(max_length=30)
    bod_eliminado = models.CharField(max_length=2,default='no')

class Articulo(models.Model):
    art_id=models.AutoField(primary_key=True)
    art_nombre = models.CharField(max_length=30)
    art_eliminado = models.CharField(max_length=2,default='no')

class DetalleBodega(models.Model):
    det_bod_id = models.AutoField(primary_key=True)
    det_bod_bod = models.ForeignKey(Bodega, on_delete=models.DO_NOTHING, null=True) #models.setNull
    det_bod_art = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING, null=True)
    det_bod_cantidad = models.PositiveIntegerField()
    det_bod_eliminado = models.CharField(max_length=2,default='no')


    #class Meta:
        #managed = False
        #db_table = 'detalle' 