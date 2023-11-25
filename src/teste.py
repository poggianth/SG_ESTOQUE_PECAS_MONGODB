from controller.controller_estoque import Controller_Estoque
from controller.controller_produto import Controller_Produto
from reports.relatorios import Relatorio

controller_estoque = Controller_Estoque()
controller_produto = Controller_Produto()
relatorios = Relatorio()


# Métodos que estão funcionando:

# Relatórios
# relatorios.get_estoque_produto_em_estoque_especifico()
# relatorios.get_estoque_todos_estoques()
# relatorios.get_item__todos_itens()
# relatorios.get_produto_todos_produtos()

# Controller estoque
# controller_estoque.inserir_estoque()
# controller_estoque.excluir_estoque()
# controller_estoque.alterar_estoque()

# Controller produto
# controller_produto.inserir_produto()
# controller_produto.alterar_produto()
# controller_produto.excluir_produto()



