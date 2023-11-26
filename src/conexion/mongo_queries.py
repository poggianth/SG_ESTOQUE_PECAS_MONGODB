import pymongo

class MongoQueries:
    def __init__(self):
        # Laboratório:
        self.host = "localhost"
        self.port = 27017
        self.service_name = 'labdatabase'
        self.user = 'labdatabase'
        self.passwd = 'labDatabase2022'
    
    
    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        # Crie uma instância do cliente MongoDB
        self.mongo_client = pymongo.MongoClient(self.host, self.port)

        # Conecte-se ao servidor MongoDB
        self.db = self.mongo_client[self.service_name]

    def close(self):
        self.mongo_client.close()