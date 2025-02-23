# =============================================================================
# Seção: Imports
# =============================================================================
import locale
from django.db import models
import hashlib
from decimal import Decimal, ROUND_HALF_UP

# =============================================================================
# Seção: Modelos de Dados
# =============================================================================

# -----------------------------------------------------------------------------
# Modelo: Categoria
# -----------------------------------------------------------------------------
class Categoria(models.Model):
    nome  = models.CharField(max_length=100)
    ordem = models.IntegerField()

    def __str__(self):
        return self.nome


# -----------------------------------------------------------------------------
# Modelo: Cliente
# -----------------------------------------------------------------------------
class Cliente(models.Model):
    nome     = models.CharField(max_length=100)
    cpf      = models.CharField(max_length=15, verbose_name="C.P.F")
    datanasc = models.DateField(verbose_name="Data de Nascimento")

    def __str__(self):
        return self.nome

    @property
    def datanascimento(self):
        """Retorna a data de nascimento no formato DD/MM/AAAA."""
        if self.datanasc:
            return self.datanasc.strftime('%d/%m/%Y')
        return None


# -----------------------------------------------------------------------------
# Modelo: Produto
# -----------------------------------------------------------------------------
class Produto(models.Model):
    nome      = models.CharField(max_length=100)
    preco     = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img_base64 = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    @property
    def estoque(self):
        estoque_item, criado = Estoque.objects.get_or_create(produto=self, defaults={'qtde': 0})
        return estoque_item


# -----------------------------------------------------------------------------
# Modelo: Estoque
# -----------------------------------------------------------------------------
class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde    = models.IntegerField()

    def __str__(self):
        return f'{self.produto.nome} - Quantidade: {self.qtde}'


# -----------------------------------------------------------------------------
# Modelo: Pedido
# -----------------------------------------------------------------------------
class Pedido(models.Model):
    # Constantes para status
    NOVO         = 1
    EM_ANDAMENTO = 2
    CONCLUIDO    = 3
    CANCELADO    = 4

    STATUS_CHOICES = [
        (NOVO, 'Novo'),
        (EM_ANDAMENTO, 'Em Andamento'),
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado'),
    ]

    cliente     = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos    = models.ManyToManyField(Produto, through='ItemPedido', related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status      = models.IntegerField(choices=STATUS_CHOICES, default=NOVO)

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nome} - Status: {self.get_status_display()}"

    @property
    def data_pedidof(self):
        if self.data_pedido:
            return self.data_pedido.strftime('%d/%m/%Y %H:%M')
        return None

    @property
    def total(self):
        return sum(item.qtde * item.preco for item in self.itens.all())

    @property
    def qtdeItens(self):
        return self.itens.count()

    @property
    def pagamentos(self):
        return Pagamento.objects.filter(pedido=self)

    @property
    def total_pago(self):
        return sum(pag.valor for pag in self.pagamentos.all())

    @property
    def debito(self):
        return self.total - self.total_pago

    @property
    def data_pedido_key(self):
        if self.data_pedido:
            return self.data_pedido.strftime('%Y%m%d')
        return None

    @property
    def chave_acesso(self):
        # Gera a chave de acesso combinando o ID e a data do pedido
        if self.id and self.data_pedido_key:
            dados_combinados = f"{self.id}{self.data_pedido_key}"
            hash_sha = hashlib.sha256()
            hash_sha.update(dados_combinados.encode('utf-8'))
            chave = f"{self.data_pedido_key}{self.id}{hash_sha.hexdigest()}"
            chave_numerica = ''.join(filter(str.isdigit, chave))
            return chave_numerica
        return None

    @property
    def calculoICMS(self):
        icms_taxa = Decimal('0.18')
        calculo = (self.total * icms_taxa).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        print(f"TOTAL: {self.total}")
        return calculo

    @property
    def calculoIPI(self):
        ipi_taxa = Decimal('0.05')
        return (self.total * ipi_taxa).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @property
    def calculoPIS(self):
        pis_taxa = Decimal('0.0165')
        return (self.total * pis_taxa).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @property
    def calculoCONFINS(self):
        confins_taxa = Decimal('0.076')
        return (self.total * confins_taxa).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @property
    def total_impostos(self):
        impostos = (self.calculoICMS + self.calculoIPI + self.calculoPIS + self.calculoCONFINS)
        return impostos.quantize(Decimal('0.010'), rounding=ROUND_HALF_UP)

    @property
    def valor_final(self):
        return (self.total + self.total_impostos).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


# -----------------------------------------------------------------------------
# Modelo: ItemPedido
# -----------------------------------------------------------------------------
class ItemPedido(models.Model):
    pedido   = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto  = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde     = models.PositiveIntegerField()
    preco    = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} (Qtde: {self.qtde}) - Preço Unitário: {self.preco}"

    @property
    def calculoTotal(self):
        return self.qtde * self.produto.preco

    @property
    def total(self):
        # Soma o total de itens relacionados (caso existam sub-itens)
        return sum(item.qtde * item.preco for item in self.itempedido_set.all())


# -----------------------------------------------------------------------------
# Modelo: Pagamento
# -----------------------------------------------------------------------------
class Pagamento(models.Model):
    DINHEIRO = 1
    CREDITO  = 2
    DEBITO   = 3
    PIX      = 4
    TICKET   = 5
    OUTRA    = 6

    FORMA_CHOICES = [
        (DINHEIRO, 'Dinheiro'),
        (CREDITO, 'Credito'),
        (DEBITO, 'Debito'),
        (PIX, 'Pix'),
        (TICKET, 'Ticket'),
        (OUTRA, 'Outra'),
    ]

    pedido   = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    forma    = models.IntegerField(choices=FORMA_CHOICES)
    valor    = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    data_pgto = models.DateTimeField(auto_now_add=True)

    @property
    def data_pgtof(self):
        """Retorna a data formatada no padrão DD/MM/AAAA HH:MM."""
        if self.data_pgto:
            return self.data_pgto.strftime('%d/%m/%Y %H:%M')
        return None
