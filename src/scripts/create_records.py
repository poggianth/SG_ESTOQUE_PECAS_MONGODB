from pymongo import MongoClient

# Conectando ao servidor MongoDB
client = MongoClient('localhost', 27017)
db = client['labdatabase']

try:
    # Inserindo registros na coleção 'estoques'
    estoques = [
        {"codigo": 1, "tipo": "Estoque A"},
        {"codigo": 2, "tipo": "Estoque B"},
        {"codigo": 3, "tipo": "Estoque C"},
        {"codigo": 4, "tipo": "Estoque D"},
        {"codigo": 5, "tipo": "Estoque E"}
    ]
    db.estoques.insert_many(estoques)
    print("Registros em estoques inseridos com sucesso!")

    # Inserindo registros na coleção 'produtos'
    produtos = [
        {"codigo": 1, "nome": "Produto 1", "descricao": "Descrição do Produto 1", "quantidade": 10, "categoria": "Categoria 1", "preco_unitario": 100},
        {"codigo": 2, "nome": "Produto 2", "descricao": "Descrição do Produto 2", "quantidade": 20, "categoria": "Categoria 2", "preco_unitario": 200},
        {"codigo": 3, "nome": "Produto 3", "descricao": "Descrição do Produto 3", "quantidade": 30, "categoria": "Categoria 3", "preco_unitario": 300},
        {"codigo": 4, "nome": "Produto 4", "descricao": "Descrição do Produto 4", "quantidade": 40, "categoria": "Categoria 4", "preco_unitario": 400},
        {"codigo": 5, "nome": "Produto 5", "descricao": "Descrição do Produto 5", "quantidade": 50, "categoria": "Categoria 5", "preco_unitario": 500}
    ]
    db.produtos.insert_many(produtos)
    print("Registros em produtos inseridos com sucesso!")

    # Inserindo registros na coleção 'itens_estoque'
    itens_estoque = [
        {"codigo": 1, "codigo_estoque": 1, "codigo_produto": 1, "estante": "A", "prateleira": "1"},
        {"codigo": 2, "codigo_estoque": 1, "codigo_produto": 2, "estante": "B", "prateleira": "2"},
        {"codigo": 3, "codigo_estoque": 2, "codigo_produto": 3, "estante": "C", "prateleira": "3"},
        {"codigo": 4, "codigo_estoque": 2, "codigo_produto": 4, "estante": "D", "prateleira": "4"},
        {"codigo": 5, "codigo_estoque": 3, "codigo_produto": 5, "estante": "E", "prateleira": "5"},
        {"codigo": 6, "codigo_estoque": 2, "codigo_produto": 3, "estante": "F", "prateleira": "8"},
        {"codigo": 7, "codigo_estoque": 3, "codigo_produto": 4, "estante": "G", "prateleira": "10"},
        {"codigo": 8, "codigo_estoque": 3, "codigo_produto": 5, "estante": "H", "prateleira": "12"}
    ]
    db.itens_estoque.insert_many(itens_estoque)
    print("Registros em itens_estoque inseridos com sucesso!")

except Exception as error:
    print(f"Erro ao inserir registros: {error}")

client.close()
