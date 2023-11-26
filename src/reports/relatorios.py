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
        mongo = MongoQueries()
        mongo.connect()
        produtos_collection = mongo.db["produtos"]


        # Agregação para calcular o valor total por produto e o valor total geral
        pipeline = [
            {
                "$project": {
                    "Produto_ID": "$_id",
                    "Produto_Nome": "$nome",
                    "Quantidade": "$quantidade",
                    "Preco_Unitario": "$preco_unitario",
                    "ValorTotalPorProduto": {"$multiply": ["$quantidade", "$preco_unitario"]}
                }
            },
            {
                "$group": {
                    "_id": None,
                    "Produtos": {
                        "$push": {
                            "Produto_ID": "$Produto_ID",
                            "Produto_Nome": "$Produto_Nome",
                            "Quantidade": "$Quantidade",
                            "Preco_Unitario": "$Preco_Unitario",
                            "ValorTotalPorProduto": "$ValorTotalPorProduto"
                        }
                    },
                    "ValorTotalGeral": {"$sum": "$ValorTotalPorProduto"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "Produtos": 1,
                    "Total_Geral": {
                        "Produto_ID": "-------------",
                        "Produto_Nome": "Total Geral",
                        "Quantidade": "-------------",
                        "Preco_Unitario": "-------------",
                        "ValorTotalPorProduto": "$ValorTotalGeral"
                    }
                }
            }
        ]

        result = list(produtos_collection.aggregate(pipeline))
        
        if not result:
            print("Não existe nenhum produto cadastrado!")
        else:
            # Criando dataframes com os resultados
            df_produtos = pd.DataFrame(result[0]['Produtos'])
            df_total_geral = pd.DataFrame([result[0]['Total_Geral']])

            print("Produtos:")
            print(df_produtos)
            print("\nTotal Geral:")
            print(df_total_geral)

        mongo.close()
        input("\nPressione Enter para Sair do Relatório de Produtos ")

    
    def get_produto_produtos_reposicao(self):
        mongo = MongoQueries()
        mongo.connect()
        produtos_collection = mongo.db["produtos"]

        # Consulta para encontrar produtos que precisam de reposição
        query_produto_reposicao = {"$expr": {"$lte": ["$quantidade", "$quantidade_reposicao"]}}
        result = list(produtos_collection.find(query_produto_reposicao).sort([("id", 1)]))

        if not result:
            print("Nenhum produto precisa de reposição! :)")
        else:
            # Criando um DataFrame com os resultados
            df_produtos_reposicao = pd.DataFrame(result)
            print(df_produtos_reposicao)

        mongo.close()
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
                produtos_em_estoque = mongo.db["itens_estoque"].find({"codigo_estoque": codigo_estoque})
                df_produtos_em_estoque = pd.DataFrame(produtos_em_estoque)

                if df_produtos_em_estoque.empty:
                    print(f"Não existem produtos armazenados no estoque ({codigo_estoque})")
                else:
                    print(f"Produtos armazenados no estoque {codigo_estoque}: ")
                    print(df_produtos_em_estoque)

            input("\nPressione Enter para sair do Relatório de Estoque ")

        except Exception as error:
            print(f"[OPS] - Erro ao buscar produtos no estoque: {error}")
        
        mongo.close()

    
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
        codigo_produto = int(input("Informe o id do produto: "))

        try:
            mongo = MongoQueries()
            mongo.connect()

            result = mongo.db["itens_estoque"].find({
                "codigo_produto": codigo_produto
            })

            df_localizacao_produto = pd.DataFrame(result)


            if df_localizacao_produto.empty:
                print(f"O produto ({codigo_produto}) não está armazenado em nenhum estoque ou não existe!")
            else:
                # Criando um DataFrame com os resultados
                print(df_localizacao_produto)
        except Exception as error:
            print(f"Erro ao buscar localização de um produto: {error}")

        mongo.close()
        input("\nPressione Enter para sair do Relatório de Itens ")