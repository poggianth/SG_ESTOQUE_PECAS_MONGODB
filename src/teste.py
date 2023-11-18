import pymongo

# Estabelecer a conexão com o servidor do MongoDB
client = pymongo.MongoClient("localhost", 27017)  # Mude "localhost" e a porta se o MongoDB estiver em outro lugar

# Acessar o banco de dados (ou criar um novo)
db = client['SG_ESTOQUE_PECAS']  # Substitua 'nome_do_banco_de_dados' pelo nome do seu banco de dados

# Acessar uma coleção dentro do banco de dados (ou criar uma nova)
collection = db['produtos']  # Substitua 'nome_da_colecao' pelo nome da sua coleção

# # Exemplo: Inserir um documento na coleção
# data = {'chave': 'valor'}  # Seus dados aqui
# collection.insert_one(data)

# Exemplo: Consultar dados na coleção
# result = collection.find_one({'chave': 'valor'})  # Consulta um documento com a chave 'valor'
result = collection.find_one()
print("result: ", result)

# # Exemplo: Atualizar um documento na coleção
# update_data = {'$set': {'nova_chave': 'novo_valor'}}
# collection.update_one({'chave': 'valor'}, update_data)  # Atualiza o documento onde a chave é 'valor'

# Fechar a conexão com o MongoDB (opcional)
client.close()
