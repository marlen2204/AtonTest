from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.currency} ({self.date}): {self.rate}"
