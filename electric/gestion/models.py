from django.db import models

class Ganaderos(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Ganado(models.Model):
    numero_identificacion = models.CharField(max_length=100, unique=True)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    peso = models.FloatField()
    dueño = models.ForeignKey(Ganaderos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.numero_identificacion} - {self.especie} ({self.dueño.nombre})'

class Compra(models.Model):
    ganado = models.ForeignKey(Ganado, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Ganaderos, related_name='compras', on_delete=models.CASCADE)
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Compra de {self.ganado.numero_identificacion} por {self.comprador.nombre}'

class Venta(models.Model):
    ganado = models.ForeignKey(Ganado, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Ganaderos, related_name='ventas', on_delete=models.CASCADE)
    comprador = models.CharField(max_length=100) 
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venta de {self.ganado.numero_identificacion} por {self.vendedor.nombre}'

class Traspaso(models.Model):
    ganado = models.ForeignKey(Ganado, on_delete=models.CASCADE)
    dueño_original = models.ForeignKey(Ganaderos, related_name='traspasos_origen', on_delete=models.CASCADE)
    dueño_destino = models.ForeignKey(Ganaderos, related_name='traspasos_destino', on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f'Traspaso de {self.ganado.numero_identificacion} de {self.dueño_original.nombre} a {self.dueño_destino.nombre}'