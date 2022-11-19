from django.utils import timezone
from django.db import models
from django.utils.html import format_html
from django.db import models
from django.contrib import admin
from gerenciador.settings import MEDIA_ROOT_ADMIN


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Eletricista(models.Model):
    STATUS = (
        ("Reparada", "Reparada"),
        ("Aguardando material", "Aguardando material"),
        ("Danificado", "Danificado"),
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=15, blank=True, null=True)  # string 15
    area = models.ForeignKey(
        "utils.Area",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Área",
    )

    cargo = models.CharField(max_length=40, blank=True, null=True)
    imagem = models.ImageField(
        "Foto de Perfil",
        upload_to='NR10/foto/',
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.nome}"


    @admin.display()
    def showImg(self):
        path = str(self.imagem).replace("/", "\\")
        run = format_html(
            f"""<img
            style="width:60px; height: 50px;"
            src="{MEDIA_ROOT_ADMIN}\{path}"
            >""",
        )
        return run


class Nr10(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(Eletricista, related_name="nr10", on_delete=models.CASCADE)
    data = models.DateField()
    certificado = models.FileField(upload_to ='NR10/NR10/', max_length=254)

    def expiracao(self):
        data_expiracao = "2 anos"
    
    class Meta:
        verbose_name_plural = "NR10 Complementar"
        verbose_name = 'NR10 Complementar'
        ordering = ['id']

    def __str__(self):
        return f"NR10 de {self.dono}"


class Nr10Complementar(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(
        Eletricista, related_name="nr10_Complementar", on_delete=models.CASCADE
    )
    data = models.DateField()
    certificado = models.FileField(upload_to ='NR10/NR10Complementar/', max_length=254)

    def expiracao(self):
        data_expiracao = "2 anos"
        
    class Meta:
        verbose_name_plural = "NR10's Complementares"
        verbose_name = 'NR10 Complementar'
        ordering = ['id']
        
    def __str__(self):
        return f"NR10 de {self.dono}"
        
class Asu(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(Eletricista, related_name="Asu", on_delete=models.CASCADE)
    data = models.DateField()
    certificado = models.FileField(upload_to ='NR10/ASU/', max_length=254)

    def expiracao(self):
        data_expiracao = "1 anos"
    
    class Meta:
        verbose_name = 'ASU'
        verbose_name_plural = "ASU's"

    def __str__(self):
        return f"ASU de {self.dono}"
