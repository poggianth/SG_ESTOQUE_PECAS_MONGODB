from conexion.mongo_queries import MongoQueries
from reports import relatorios
import pandas as pd

relatorio = relatorios.Relatorio()


class Controller_Estoque:
    def __init__(self):
        self.mongo = MongoQueries()
        self.collection_name = "estoques"

    def existe_estoque(self, codigo_estoque: int):
        self.mongo.connect()
        result = self.mongo.db[self.collection_name].find_one(
            {"codigo": codigo_estoque})

        return not result == None

    def inserir_estoque(self):
        self.mongo.connect()

        tipo_estoque = input("Informe o tipo: ")

        try:
            ultimo_codigo = self.mongo.db[self.collection_name].find_one(
                {}, sort=[("codigo", -1)])["codigo"]
            # qtd_estoques = self.mongo.db[self.collection_name].count_documents({})
            self.mongo.db[self.collection_name].insert_one(
                {"tipo": tipo_estoque, "codigo": ultimo_codigo+1})
            print("\nEstoque inserido com sucesso!")

            print("""\nDeseja inserir um novo estoque?
              [1] - Sim
              [0] - Não""")
            opcao_novamente = int(input("Informe sua opção: "))

            if opcao_novamente == 1:
                self.inserir_estoque()

        except Exception as error:
            print(f"[OPS] - Erro ao inserir estoque: {error}")

        self.mongo.close()

    def alterar_estoque(self):
        if relatorio.get_estoque_todos_estoques():
            codigo_estoque_alterar = int(
                input("\nInforme o código(id) do estoque que irá ALTERAR: "))

            try:
                self.mongo.connect()

                if self.existe_estoque(codigo_estoque_alterar):
                    tipo_estoque_novo = input("Informe o (NOVO) tipo: ")

                    # Atualiza o tipo do estoque
                    self.mongo.db[self.collection_name].update_one(
                        {"codigo": codigo_estoque_alterar}, {"$set": {"tipo": tipo_estoque_novo}})
                    print(
                        f"Estoque({codigo_estoque_alterar}) alterado com sucesso!")

                    opcao_novamente = int(input("""\nDeseja alterar um novo estoque?
                                                [1] - Sim
                                                [0] - Não
                                                Informe sua opção: """))

                    if opcao_novamente == 1:
                        self.alterar_estoque()
                else:
                    print(f"Não existe nenhum estoque com o código(id) = {
                          codigo_estoque_alterar}")

            except Exception as error:
                print(f"[OPS] - Erro ao atualizar estoque: {error}")
        else:
            print(
                "Não existe nenhum estoque cadastrado para ALTERAR! Cadastre pelo menos 1")

        self.mongo.close()

    def excluir_estoque(self):
        if relatorio.get_estoque_todos_estoques():
            codigo_estoque_excluir = int(
                input("\nInforme o código(id) do estoque que irá EXCLUIR: "))

            try:
                self.mongo.connect()

                if self.existe_estoque(codigo_estoque_excluir):
                    dependentes_encontrados = self.mongo.db["itens_estoque"].find(
                        {"codigo_estoque": codigo_estoque_excluir})
                    df_dependentes_encontrados = pd.DataFrame(
                        dependentes_encontrados)
                    possuiDependentes = False

                    if not df_dependentes_encontrados.empty:
                        possuiDependentes = True
                        print(f"\nForam encontrados produtos armazenados no estoque ({
                              codigo_estoque_excluir}):\n")
                        print(df_dependentes_encontrados)

                    print("""\nTem certeza que deseja excluir o estoque selecionado (também irá excluir os produtos armazenados)?
                    [1] - Sim
                    [0] - Não""")
                    opcao_certeza = int(input("Informe sua opção: "))

                    if opcao_certeza == 1:
                        if possuiDependentes:
                            self.mongo.db["itens_estoque"].delete_many(
                                {"codigo_estoque": codigo_estoque_excluir})

                        self.mongo.db[self.collection_name].delete_one(
                            {"codigo": codigo_estoque_excluir})

                        print(
                            f"Estoque({codigo_estoque_excluir}) excluído com sucesso!")
                    elif opcao_certeza == 0:
                        print("Operação de exclusão cancelada com sucesso!")
                    else:
                        print("Opção inválida!")
                else:
                    print(f"Não existe nenhum estoque com o código(id) = {
                          codigo_estoque_excluir}")

            except Exception as error:
                print(f"[OPS] - Erro ao excluir estoque: ${error}")
        else:
            print(
                "Não existe nenhum estoque cadastrado para EXCLUIR! Cadastre pelo menos 1")
        self.mongo.close()
