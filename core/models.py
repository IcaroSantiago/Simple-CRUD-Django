from django.db import models


class Produtos(models.Model):
    nome = models.CharField(max_length=70, blank=False)
    preco = models.IntegerField()
    quantidade = models.IntegerField()

    choices = {
        ('Disponivel', 'Este item esta disponivel'),
        ('Indisponivel', 'Este item acabou'),
        ('Abastecer','Esta item esta acabando')
    }
    status = models.CharField(max_length=20,choices=choices,default="Indisponivel")

    def __str__(self):
        return 'Nome:{0} Preco:{1} Status{2}'.format(self.nome, self.preco)
    
