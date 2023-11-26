from conexion.mongo_queries import MongoQueries
from reports import relatorios
from controller import controller_estoque, controller_produto

control_estoque = controller_estoque.Controller_Estoque()
control_produto = controller_produto.Controller_Produto()
relatorio = relatorios.Relatorio()


class Controller_Item_Estoque:
    def __init__(self):
        self.mongo = MongoQueries()
        self.collection_name = "itens_estoque"

    def existe_item_estoque(self, codigo_item_estoque: int):
        self.mongo.connect()
        result = self.mongo.db[self.collection_name].find_one(
            {"codigo": codigo_item_estoque})

        return not result == None

    def inserir_item_estoque(self):
        try:
            self.mongo.connect()
            ultimo_codigo = self.mongo.db[self.collection_name].find_one(
                {}, sort=[("codigo", -1)])["codigo"]

            if relatorio.get_produto_todos_produtos():
                codigo_produto = int(
                    input("Informe o código(id) do produto que deseja armazenar: "))

                if control_produto.existe_produto(codigo_produto):
                    if relatorio.get_estoque_todos_estoques():
                        codigo_estoque = int(
                            input("Informe o código(id) do estoque onde irá armazenar: "))
                        if control_estoque.existe_estoque(codigo_estoque):
                            estante = input(
                                "Informe a estante onde o produto ficará: ")
                            prateleira = int(
                                input("Informe o número da prateleira: "))

                            self.mongo.db[self.collection_name].insert_one({
                                "codigo_estoque": codigo_estoque,
                                "codigo_produto": codigo_produto,
                                "estante": estante,
                                "prateleira": prateleira,
                                "codigo": ultimo_codigo + 1
                            })

                            print("\nProduto armazenado com sucesso!")

                            print("""\nDeseja armazenar mais um produto?
                                    [1] - Sim
                                    [0] - Não""")
                            opcao_novamente = int(input("Informe sua opção: "))

                            if opcao_novamente == 1:
                                self.inserir_item_estoque()

                        else:
                            print(
                                f"[OPS] - Não existe nenhum estoque com o código(id) = {codigo_estoque}")
                    else:
                        print(
                            "Cadastre pelo menos 1 estoque antes de guardar o produto!")
                else:
                    print(
                        f"[OPS] - Não existe nenhum produto com o código = {codigo_produto}")
            else:
                print("Cadastre pelo menos 1 produto antes de guardá-lo!")
        except Exception as error:
            print(f"[OPS] - Erro ao armazenar produto: {error}")

        self.mongo.close()

    def alterar_item_estoque(self):
        # Mostra os itens_armazenados para guiar o usuário
        if relatorio.get_item__todos_itens():
            codigo_item_estoque_alterar = int(
                input("Informe o código(id) do item_produto que deseja alterar: "))

            try:
                if self.existe_item_estoque(codigo_item_estoque_alterar):
                    if relatorio.get_produto_todos_produtos():
                        codigo_produto = int(
                            input("Informe o (NOVO) código(id) do produto que deseja armazenar: "))
                        if control_produto.existe_produto(codigo_produto):
                            if relatorio.get_estoque_todos_estoques():
                                codigo_estoque = int(
                                    input("Informe o (NOVO) código(id) do estoque onde irá armazenar: "))
                                if control_estoque.existe_estoque(codigo_estoque):
                                    estante = input(
                                        "Informe a (NOVA) estante onde o produto ficará: ")
                                    prateleira = int(
                                        input("Informe o (NOVO) número da prateleira: "))

                                    self.mongo.db[self.collection_name].update_one({"codigo": codigo_item_estoque_alterar}, {"$set": {
                                        "codigo_estoque": codigo_estoque,
                                        "codigo_produto": codigo_produto,
                                        "estante": estante,
                                        "prateleira": prateleira
                                    }})

                                    print(
                                        "\nLocalização do produto alterada com sucesso!")

                                    print("""\nDeseja alterar a localização de mais um produto?
                                    [1] - Sim
                                    [0] - Não""")
                                    opcao_novamente = int(
                                        input("Informe sua opção: "))

                                    if opcao_novamente == 1:
                                        self.alterar_item_estoque()

                                else:
                                    print(
                                        f"[OPS] - Não existe nenhum estoque com o código(id) = {codigo_estoque}")
                            else:
                                print(
                                    "Cadastre pelo menos 1 estoque antes de guardar o produto!")
                        else:
                            print(
                                f"[OPS] - Não existe nenhum produto com o código = {codigo_produto}")
                    else:
                        print("Cadastre pelo menos 1 produto antes de guardá-lo!")
                else:
                    print(f"Não existe nenhum item_estoque com o código(id) = {
                          codigo_item_estoque_alterar}")

            except Exception as error:
                print(f"[OPS] - Erro ao editar item_estoque: {error}")

        else:
            print(
                "Não existe nenhum produto armazenado para ALTERAR! Armazene pelo menos 1")
        self.mongo.close()

    def excluir_item_estoque(self):
        # Mostra os itens_armazenados para guiar o usuário
        if relatorio.get_item__todos_itens():
            codigo_item_estoque_excluir = int(
                input("\nInforme o código(id) do item_estoque que irá EXCLUIR: "))

            try:
                self.mongo.connect()

                if self.existe_item_estoque(codigo_item_estoque_excluir):
                    print("""\nTem certeza que deseja excluir o item_estoque selecionado?
                    [1] - Sim
                    [0] - Não""")
                    opcao_certeza = int(input("Informe sua opção: "))

                    if opcao_certeza == 1:
                        self.mongo.db[self.collection_name].delete_one(
                            {"codigo": codigo_item_estoque_excluir})

                        print(
                            f"Item_estoque({codigo_item_estoque_excluir}) excluído com sucesso!")
                    else:
                        print("Operação de exclusão cancelada com sucesso!")
                else:
                    print(f"Não existe nenhum item_estoque com o código = {
                          codigo_item_estoque_excluir}")
            except Exception as error:
                print(f"[OPS] - Erro ao excluir item_estoque: {error}")

        else:
            print(
                "Não existe nenhum produto armazenado para ALTERAR! Armazene pelo menos 1")

        self.mongo.close()
