from view import menu

class SplashScreen:
    def __init__(self):
        self.created_by = """
                    FABIO GONÇALVES, 
                    MARCELO MIRANDA,
                    NICOLAS RODRIGUES
                    THIAGO MELO"""
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"
        
    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = menu.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]


    def get_updated_screen(self):
        return(
        f"""
        =-=-=-=-=-=-=-=-=-=-=-=-= GESTÃO DE ESTOQUE =-=-=-=-=-=-=-=-=-=-=-=-=
        
            Total de registros existentes:
                1 - ESTOQUE:                {str(self.get_documents_count(collection_name="estoques")).rjust(5)}
                2 - PRODUTO:                {str(self.get_documents_count(collection_name="produtos")).rjust(5)}
                3 - ITEM_ESTOQUE:           {str(self.get_documents_count(collection_name="itens_estoque")).rjust(5)}
            
            ------------------------------------
            Criado por: {self.created_by}

            Professor: {self.professor}
            
            DISCIPLINA: {self.disciplina}
                        {self.semestre}
            ------------------------------------

        {"=-=" * 23}
        """
        )