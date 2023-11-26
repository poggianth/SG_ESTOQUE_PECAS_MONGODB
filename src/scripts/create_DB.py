from pymongo import MongoClient

# Conectando ao servidor MongoDB
mongo = MongoClient('localhost', 27017)

# Criando o banco de dados
db = mongo['labdatabase']

# Criando coleções dentro do banco de dados
colecoes = ['estoques', 'produtos', 'itens_estoque']

for colecao in colecoes:
    db.create_collection(colecao)
    print(f"Coleção '{colecao}' criada com sucesso!")

mongo.close()
