from django.db import models

class Cotacao(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cotação'
        verbose_name_plural = 'Cotações'
        ordering = ('-created_at', 'is_active')

    

class Wallet(models.Model):

    close = models.CharField(max_length=10)
    high = models.CharField(max_length=10)
    low = models.CharField(max_length=10)
    open = models.CharField(max_length=10)
    volume = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Wallets'
        verbose_name_plural = 'Wallet'
        ordering = ('-created_at', 'is_active', 'updated_at')



