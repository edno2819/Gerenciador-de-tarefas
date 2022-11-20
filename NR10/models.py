from django.utils import timezone as tz
from django.db import models
from django.utils.html import format_html
from django.db import models
from django.contrib import admin
from gerenciador.settings import MEDIA_ROOT_ADMIN
import datetime


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return tz.now()


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
        upload_to="NR10/foto/",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.nome}"

    @admin.display(description="Asu")
    def expire_asu(self):
        last_asu = Asu.objects.filter(dono=self.id).latest("data")
        delta = ((last_asu.data + datetime.timedelta(days=last_asu.expiracao)) - datetime.date.today()).days
        if int(delta)>0:
            return format_html(f'''<div
            style="background-color: #319c35; border:#319c35 ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expira em {int(delta)} dias</div>''')
        else:
            return format_html(f'''<div
            style="background-color: #a71c1c; border:#a71c1c ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expirado à {int(delta) * -1} dias </div>''')
            
    @admin.display(description="Nr10")
    def expire_Nr10(self):
        last_Nr10 = Nr10.objects.filter(dono=self.id).latest("data")
        delta = ((last_Nr10.data + datetime.timedelta(days=last_Nr10.expiracao)) - datetime.date.today()).days
        if int(delta)>0:
            return format_html(f'''<div
            style="background-color: #319c35; border:#319c35 ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expira em {int(delta)} dias</div>''')
        else:
            return format_html(f'''<div
            style="background-color: #a71c1c; border:#a71c1c ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expirado à {int(delta) * -1} dias </div>''')

    @admin.display(description="Nr10Complementar")
    def expire_Nr10Complementar(self):
        last_Nr10Complementar = Nr10Complementar.objects.filter(dono=self.id).latest("data")
        delta = ((last_Nr10Complementar.data + datetime.timedelta(days=last_Nr10Complementar.expiracao)) - datetime.date.today()).days
        if int(delta)>0:
            return format_html(f'''<div
            style="background-color: #319c35; border:#319c35 ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expira em {int(delta)} dias</div>''')
        else:
            return format_html(f'''<div
            style="background-color: #a71c1c; border:#a71c1c ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expirado à {int(delta) * -1} dias </div>''')   

    @admin.display(description="Autorizacao")
    def expire_Autorizacao(self):
        last_Autorizacao = Autorizacao.objects.filter(dono=self.id).latest("data")
        delta = ((last_Autorizacao.data + datetime.timedelta(days=last_Autorizacao.expiracao)) - datetime.date.today()).days
        if int(delta)>0:
            return format_html(f'''<div
            style="background-color: #319c35; border:#319c35 ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expira em {int(delta)} dias</div>''')
        else:
            return format_html(f'''<div
            style="background-color: #a71c1c; border:#a71c1c ;color: rgb(255, 255, 255); border-radius: 5px;
            padding:5px"
            > Expirado à {int(delta) * -1} dias </div>''')   


    @admin.display(description="Nivel Autorização")
    def autorizacao(self):
        last_auto = Autorizacao.objects.filter(dono=self.id).latest("data")
        return last_auto


class Nr10(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(Eletricista, related_name="nr10", on_delete=models.CASCADE)
    data = models.DateField()
    certificado = models.FileField(upload_to="NR10/NR10/", max_length=254)

    @property
    def expiracao(self):
        dias_expiracao = 365 *2
        return dias_expiracao

    class Meta:
        verbose_name_plural = "NR10 Complementar"
        verbose_name = "NR10 Complementar"
        ordering = ["id"]

    def __str__(self):
        return f"NR10 de {self.dono}"


class Nr10Complementar(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(
        Eletricista, related_name="nr10_Complementar", on_delete=models.CASCADE
    )
    data = models.DateField()
    certificado = models.FileField(upload_to="NR10/NR10Complementar/", max_length=254)

    @property
    def expiracao(self):
        dias_expiracao = 365 *2
        return dias_expiracao

    class Meta:
        verbose_name_plural = "NR10's Complementares"
        verbose_name = "NR10 Complementar"
        ordering = ["id"]

    def __str__(self):
        return f"NR10 de {self.dono}"


class Asu(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(Eletricista, related_name="Asu", on_delete=models.CASCADE)
    data = models.DateField()
    certificado = models.FileField(upload_to="NR10/ASU/", max_length=254)

    @property
    def expiracao(self):
        dias_expiracao = 365
        return dias_expiracao


    class Meta:
        verbose_name = "ASU"
        verbose_name_plural = "ASU's"

    def __str__(self):
        return f"ASU de {self.dono}"


class Autorizacao(models.Model):
    NIVEL = (
        ("Eletrico com painel desligado", "Eletrico com painel desligado"),
        ("Eletrico com painel ligado", "Eletrico com painel ligado"),
        ("Eletrico com alta tensão", "Eletrico com alta tensão"),
        ("Completo", "Completo"),
    )
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(
        Eletricista, related_name="Autorização", on_delete=models.CASCADE
    )
    data = models.DateField()
    certificado = models.FileField(upload_to="NR10/Autorizacao/", max_length=254)
    nivel = models.CharField(
        default="Eletrico com painel desligado", max_length=254, choices=NIVEL
    )

    @property
    def expiracao(self):
        dias_expiracao = 365
        return dias_expiracao

    @property
    def get_Days(self):
        return (self.data - tz.now()).days

    class Meta:
        verbose_name = "Autorização"
        verbose_name_plural = "Autorizações"

    def __str__(self):
        return self.nivel
