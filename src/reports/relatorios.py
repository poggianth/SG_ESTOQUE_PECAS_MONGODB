from conexion.oracle_queries import OracleQueries
from conexion.mongo_queries import MongoQueries
import pandas as pd

class Relatorio:
    def __init__(self):
        pass
        

    def get_produto_todos_produtos(self):
        mongo = MongoQueries()
        mongo.connect()
        try:
            query_result = mongo.db["produtos"].find().sort([("codigo", 1)])
            df_produtos = pd.DataFrame(query_result)

            if df_produtos.empty:
                print("Não existe nenhum produto cadastrado!")
                input("\nPressione Enter para Sair do Relatório de Produtos ")
                return False
            else:
                print("Produtos armazenados: ")
                print(df_produtos)
                
                input("\nPressione Enter para Sair do Relatório de Produtos ")

                return True

        except Exception as error:
            print(f"[OPS] - Erro ao buscar produtos: {error}")
            return False
    
    
    def get_produto_valor_total(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_valor_total = """
            SELECT
                ID AS Produto_ID,
                NOME AS Produto_Nome,
                QUANTIDADE AS Quantidade,
                PRECO_UNITARIO AS Preco_Unitario,
                QUANTIDADE * PRECO_UNITARIO AS ValorTotalPorProduto
            FROM
                Produto
            UNION ALL
            SELECT
                NULL AS Produto_ID,
                'Total Geral' AS Produto_Nome,
                NULL AS Quantidade,
                NULL AS Preco_Unitario,
                SUM(QUANTIDADE * PRECO_UNITARIO) AS ValorTotalGeral
            FROM
                Produto
        """
        
        print("\n")

        result = oracle.sqlToDataFrame(query_produto_valor_total)
        if result.empty:
            print("Não existe nenhum produto cadastrado!")
        else:
            print(result)

        input("\nPressione Enter para Sair do Relatório de Produtos ")

    
    def get_produto_produtos_reposicao(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_reposicao = "SELECT * FROM produto where quantidade <= quantidade_reposicao ORDER BY (id)"

        print("\n")
        result = oracle.sqlToDataFrame(query_produto_reposicao)
        
        if result.empty:
            print("Nenhum produto precisa de reposição! :)")
        else:
            print(result)

        input("\nPressione Enter para Sair do Relatório de Produtos ")
    
    
    def get_estoque_todos_estoques(self):
        mongo = MongoQueries()
        mongo.connect()
        
        try:
            query_result = mongo.db["estoques"].find().sort([("id", 1)])
            df_todos_estoques = pd.DataFrame(query_result)

            if df_todos_estoques.empty:
                print("Não existe nenhum estoque cadastrado!")
                input("\nPressione Enter para sair do Relatório de Estoque ")
                return False
            else:
                print("Estoques cadastrados: ")
                print(df_todos_estoques)
                
                input("\nPressione Enter para sair do Relatório de Estoque ")
                return True

        except Exception as error:
            print(f"[OPS] - Erro ao buscar estoque: {error}")
            return False

        
    
    def get_estoque_produto_em_estoque_especifico(self):
        mongo = MongoQueries()
        mongo.connect()

        try:
            codigo_estoque = int(input("Informe o id do estoque: "))

            query_result = mongo.db["estoques"].find({"codigo": codigo_estoque})
            df_todos_estoques = pd.DataFrame(query_result)

            if df_todos_estoques.empty:
                print(f"Não existe nenhum estoque com o código: ({codigo_estoque})!")
            else:
                produto_ids = [item['codigo_produto'] for item in query_result]
                produtos_em_estoque = mongo.db["itens_estoque"].find({"codigo_estoque": codigo_estoque})
                df_produtos_em_estoque = pd.DataFrame(produtos_em_estoque)

                if df_produtos_em_estoque.empty:
                    print(f"Não existem produtos armazenados no estoque ({codigo_estoque})")
                else:
                    print(f"Produtos armazenados no estoque ${codigo_estoque}: ")
                    print(df_produtos_em_estoque)

            input("\nPressione Enter para sair do Relatório de Estoque ")

        except Exception as error:
            print(f"[OPS] - Erro ao buscar produtos no estoque: {error}")
    
        # id_estoque = int(input("Informe o id do estoque: "))

        # oracle = OracleQueries()
        # oracle.connect()
        # query_estoque_produto_em_estoque_especifico = f"""
        #     SELECT p.*
        #     FROM item_estoque ie
        #     INNER JOIN produto p
        #     on ie.id_produto = p.id and ie.id_estoque = {id_estoque}
        #     ORDER BY (p.id)
        #     """

        # print("\n")
        # result = oracle.sqlToDataFrame(query_estoque_produto_em_estoque_especifico)

        # if result.empty:
        #     print(f"Não existe nenhum produto no estoque ({id_estoque})")
        # else:
        #     print(result)
        
        # input("\nPressione Enter para sair do Relatório de Estoque ")

    
    def get_item__todos_itens(self):
        mongo = MongoQueries()
        mongo.connect()
        try:
            query_result = mongo.db["itens_estoque"].find().sort([("codigo", 1)])
            df_produtos_armazenados = pd.DataFrame(query_result)

            if df_produtos_armazenados.empty:
                print("Não existe nenhum produto armazenado!")
                input("\nPressione Enter para sair do Relatório de Itens_Estoque ")
                return False
            else:
                print("Produtos armazenados: ")
                print(df_produtos_armazenados)
                
                input("\nPressione Enter para sair do Relatório de Itens_Estoque ")
                return True

        except Exception as error:
            print(f"[OPS] - Erro ao buscar produto armazenado: {error}")
            return False

    
    def get_item_localizacao_produto_especifico(self):
        id_produto = int(input("Informe o id do produto: "))

        oracle = OracleQueries()
        oracle.connect()
        query_item_localizacao_produto_especifico = f"""
            SELECT distinct p.id, p.nome, p.descricao, i.estante, i.prateleira
            FROM produto p
            INNER JOIN item_estoque i
                on i.id_produto = p.id
            where i.id_produto = {id_produto}
            """

        print("\n")

        result = oracle.sqlToDataFrame(query_item_localizacao_produto_especifico)

        if result.empty:
            print(f"O produto({id_produto}) não está em nenhum estoque!")
        else:
            print(result)
        
            
        input("\nPressione Enter para sair do Relatório de Itens ")