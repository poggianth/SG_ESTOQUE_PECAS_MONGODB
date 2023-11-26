from controller.controller_estoque import Controller_Estoque
from controller.controller_produto import Controller_Produto
from controller.controller_item_estoque import Controller_Item_Estoque
from reports.relatorios import Relatorio

controller_estoque = Controller_Estoque()
controller_produto = Controller_Produto()
controller_item_estoque = Controller_Item_Estoque()
relatorios = Relatorio()


# Métodos que estão funcionando:

# Relatórios
# relatorios.get_estoque_produto_em_estoque_especifico()
# relatorios.get_estoque_todos_estoques()
# relatorios.get_item__todos_itens()
# relatorios.get_produto_todos_produtos()
# relatorios.get_produto_valor_total()
# relatorios.get_produto_produtos_reposicao()

relatorios.get_item_localizacao_produto_especifico()
# relatorios.get_estoque_produto_em_estoque_especifico()



# Controller estoque
# controller_estoque.inserir_estoque()
# controller_estoque.alterar_estoque()
# controller_estoque.excluir_estoque()

# Controller produto
# controller_produto.inserir_produto()
# controller_produto.alterar_produto()
# controller_produto.excluir_produto()

# Controller item_estoque
# controller_item_estoque.inserir_item_estoque()
# controller_item_estoque.alterar_item_estoque()
# controller_item_estoque.excluir_item_estoque()