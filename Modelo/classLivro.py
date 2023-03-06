class Livro:
    def __init__(self, id, nome, autor, paginas):
        self._id = id
        self._nome= nome
        self._autor = autor
        self._paginas = paginas

    
    def imprimirLivro(self):

        print(f'''
        ID - {self._id}
        Nome - {self._nome}
        Autor - {self._autor}
        Número de Páginas: {self._paginas}
        ''')

    def imprimirLivroDeletado(self):
        return f'''
        O Livro selecionado foi excluído!
        '''

    def listarLivros(self):
        
        sql = f'''
        SELECT * FROM "Livro" 
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def DeletarLivros(self):

        sql = f'''
        DELETE FROM "Livro"
        WHERE "ID" = {self._id}
        
        '''
        return sql
    
    def alterarLivros(self):

        sql = f'''
        UPDATE "Livro"
        SET "NomeLivro" = '{self._nome}', "Autor" = '{self._autor}', "Número de Páginas" = '{self._paginas}'
        WHERE "ID" = '{self._id}'
        '''
        return sql
        
    def consultarLivroPorID(self):
        sql = f'''
        SELECT * FROM "Livro"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def inserirLivro(self):
        sql = f'''
        INSERT INTO "Livro"
        VALUES(default, '{self._nome}', '{self._autor}', '{self._paginas}')
        
        '''

        return sql