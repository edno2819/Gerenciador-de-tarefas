from django.utils import timezone
from django.db import models
from django.db import models

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class DigitacaoProblema(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=False, null=False)
    area = models.ForeignKey(
        "utils.Area", on_delete=models.CASCADE, blank=True, null=True
    )    
    item = models.CharField(max_length=80, blank=False, null=False)
    descricao = models.CharField(default=" ", max_length=1024, blank=True)
    create_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome
