from conexion.mongo_queries import MongoQueries
from reports import relatorios
import pandas as pd

relatorio = relatorios.Relatorio()


class Controller_Produto:
    def __init__(self):
        self.mongo = MongoQueries()
        self.collection_name = "produtos"

    def existe_produto(self, codigo_produto: int):
        self.mongo.connect()
        result = self.mongo.db[self.collection_name].find_one({"codigo": codigo_produto})

        return not result == None

    def inserir_produto(self):
        self.mongo.connect()

        ultimo_codigo = self.mongo.db[self.collection_name].find_one({}, sort=[("codigo", -1)])["codigo"]

        nome = input("Informe o nome: ")
        descricao = input("Informe a descrição: ")
        quantidade = int(input("Informe a quantidade (número inteiro): "))
        categoria = input("Informe a categoria: ")
        preco_unitario = float(input("Informe o preço unitário (número decimal): "))
        quantidade_reposicao = int(input("Informe a quantidade de reposição (número inteiro): "))
        codigo = ultimo_codigo+1

        try:
            self.mongo.db[self.collection_name].insert_one({
                "codigo": codigo,
                "nome": nome,
                "descricao": descricao,
                "quantidade": quantidade,
                "categoria": categoria,
                "preco_unitario": preco_unitario,
                "quantidade_reposicao": quantidade_reposicao
            })

            print("\nProduto inserido com sucesso!")

            print("""\nDeseja inserir um novo produto?
              [1] - Sim
              [0] - Não""")
            opcao_novamente = int(input("Informe sua opção: "))

            if opcao_novamente == 1:
                self.inserir_produto()

        except Exception as error:
            print(f"[OPS] - Erro ao inserir produto: {error}")

        self.mongo.close()

    def alterar_produto(self):
        # Mostra os produtos cadastrados para guiar o usuário
        if relatorio.get_produto_todos_produtos():

            codigo_produto_alterar = int(input("\nInforme o código do produto que irá ALTERAR: "))

            try:
                self.mongo.connect()
                if self.existe_produto(codigo_produto_alterar):
                    # Produto existe
                    nome = input("Informe o (NOVO) nome: ")
                    descricao = input("Informe a (NOVA) descrição: ")
                    quantidade = int(input("Informe a (NOVA) quantidade (número inteiro): "))
                    categoria = input("Informe a (NOVA) categoria: ")
                    preco_unitario = float(input("Informe o (NOVO) preço unitário (número decimal): "))
                    quantidade_reposicao = int(input("Informe a (NOVA) quantidade de reposição (número inteiro): "))

                    self.mongo.db[self.collection_name].update_one({"codigo": codigo_produto_alterar}, {"$set": {
                        "nome": nome,
                        "descricao": descricao,
                        "quantidade": quantidade,
                        "categoria": categoria,
                        "preco_unitario": preco_unitario,
                        "quantidade_reposicao": quantidade_reposicao
                    }})

                    print(f"Produto({codigo_produto_alterar}) alterado com sucesso!")

                    print("""\nDeseja alterar mais um produto?
                    [1] - Sim
                    [0] - Não""")
                    opcao_novamente = int(input("Informe sua opção: "))

                    if opcao_novamente == 1:
                        self.alterar_produto()

                else:
                    print(f"Não existe nenhum produto com o código: {codigo_produto_alterar}")

            except Exception as error:
                print(f"[OPS] - Erro ao atualizar produto: {error}")

        else:
            print("Não existe nenhum produto cadastrado para ALTERAR! Cadastre pelo menos 1")

        self.mongo.close()

    def excluir_produto(self):
        if relatorio.get_produto_todos_produtos():
            codigo_produto_excluir = int(input("\nInforme o código do produto que irá EXCLUIR: "))

            try:
                self.mongo.connect()

                if self.existe_produto(codigo_produto_excluir):
                    dependencias_encontradas = self.mongo.db["itens_estoque"].find({"codigo_produto": codigo_produto_excluir})
                    df_dependencias_encontradas = pd.DataFrame(dependencias_encontradas)
                    possui_dependencias = False

                    if not df_dependencias_encontradas.empty:
                        possui_dependencias = True
                        print(f"\nForam encontrados produtos armazenados com o código ({codigo_produto_excluir}):\n")
                        print(df_dependencias_encontradas)

                    print("""\nTem certeza que deseja excluir o produto selecionado (também irá excluir os produtos armazenados)?
                    [1] - Sim
                    [0] - Não""")
                    opcao_certeza = int(input("Informe sua opção: "))

                    if opcao_certeza == 1:
                        if possui_dependencias:
                            self.mongo.db["itens_estoque"].delete_many({"codigo_produto": codigo_produto_excluir})

                        self.mongo.db[self.collection_name].delete_one({"codigo": codigo_produto_excluir})

                        print(f"Produto({codigo_produto_excluir}) excluído com sucesso!")
                    elif opcao_certeza == 0:
                        print("Operação de exclusão cancelada com sucesso!")
                    else:
                        print("Opção inválida!")
                else:
                    print(f"Não existe nenhum produto com o código = {codigo_produto_excluir}")

            except Exception as error:
                print(f"[OPS] - Erro ao excluir produto: {error}")

        else:
            print("Não existe nenhum produto cadastrado para EXCLUIR! Cadastre pelo menos 1")
        self.mongo.close()
