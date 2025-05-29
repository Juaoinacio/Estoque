from django.db import models

# Core == Essencial

class CarimboData(models.Model):
    criado = models.DateTimeField(
        verbose_name="criado em",
        auto_now_add=True,
        auto_now=False
    )
    modificado = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False,
        auto_now=True
    )

    # Para poder usar de herança em outras classes
    class Meta:
        abstract = True
