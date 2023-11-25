from model.produto import Produto

class ItemEstoque:
    def __init__(self,
                 id:int=None,
                 codigo_estoque:int=None,
                 codigo_produto:float=None,
                 estante:str=None,
                 prateleira:int=None,
                 produto:Produto=None
                 ):
        self.id = id
        self.codigo_estoque = codigo_estoque
        self.codigo_produto = codigo_produto
        self.estante = estante
        self.prateleira = prateleira
        self.produto = produto

    def get_codigo_estoque(self):
        return self.codigo_estoque

    def set_codigo_estoque(self, codigo_estoque):
        self.codigo_estoque = codigo_estoque

    def get_codigo_produto(self):
        return self.codigo_produto

    def set_codigo_produto(self, codigo_produto):
        self.codigo_produto = codigo_produto

    def get_estante(self):
        return self.estante

    def set_estante(self, estante):
        self.estante = estante

    def get_prateleira(self):
        return self.prateleira

    def set_prateleira(self, prateleira):
        self.prateleira = prateleira

    def get_produto(self):
        return self.produto

    def set_produto(self, produto):
        self.produto = produto

    def to_string(self):
        # Cria uma representação em string do objeto
        return f"ID Estoque: {self.codigo_estoque}\nID Produto: {self.codigo_produto}\nEstante: {self.estante}\nPrateleira: {self.prateleira}\nProduto:\n{self.produto.to_string()}"