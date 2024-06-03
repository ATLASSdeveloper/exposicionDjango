from django.db import models

class Bodega(models.Model):
    bod_id = models.AutoField(primary_key=True)
    bod_nombre = models.CharField(max_length=30)
    bod_ubicacion = models.CharField(max_length=30)

class Articulo(models.Model):
    art_id=models.AutoField(primary_key=True)
    art_nombre = models.CharField(max_length=30)

class DetalleBodega(models.Model):
    det_bod_id = models.AutoField(primary_key=True)
    det_bod_bod = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    det_bod_art = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    det_bod_cantidad = models.PositiveIntegerField()

    #class Meta:
        #managed = False
        #db_table = 'detalle' 