
from datetime import datetime
from django.db import models

# Create your models here.

##Cadastro de Locatário
class Locatario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefone =models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)

    ##Mostra por nome e email
    def __str__(self):
        return "{} - {}".format(self.nome, self.email, self.cpf)

    ##Ordena por id
    class Meta:
        verbose_name = 'Locatário'
        verbose_name_plural = 'Locatários'
        ordering = ['-id']


## Opções de Imóveis
class TipoImoveis(models.TextChoices):
    APARTMENT = 'APARTAMENTO', 'APARTAMENTO'
    KITNET = 'KITNET', 'KITNET'
    HOUSE = 'CASA', 'CASA'
    LOFT = 'LOFT', 'LOFT'


## Cadastro de Imóveis
class Imovel(models.Model):
    codigo = models.CharField(max_length=100)
    tipo_imovel = models.CharField(max_length=100, choices=TipoImoveis.choices)
    descricao = endereco = models.TextField()
    endereco = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    is_locate = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.codigo, self.tipo_imovel)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        ordering = ['-id']


## Cadastrar as Imagens do Imóvel
class ImagemImovel(models.Model):
    image = models.ImageField('Images',upload_to='images')
    Imovel = models.ForeignKey(Imovel, related_name='imovel_imagens', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Imovel.codigo

    class Meta:
        verbose_name = 'Imagem do Imóvel'
        verbose_name_plural = 'Imagens do Imóvel'
        ordering = ['-id']


## Registrar Locação
class RegistrarLocacao(models.Model):
    Imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='reg_locacao')
    Locatario = models.ForeignKey(Locatario, on_delete=models.CASCADE)
    dt_inicio = models.DateTimeField('Inicio Contrato')
    dt_fim = models.DateTimeField('Fim Contrato')
    criado = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.Locatario, self.Imovel)
    
    class Meta:
        verbose_name = 'Registrar Locação'
        verbose_name_plural = 'Registrar Locações'
        ordering = ['-id']