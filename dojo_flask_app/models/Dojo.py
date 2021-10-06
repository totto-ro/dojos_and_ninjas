from dojo_flask_app.config.MySQLConnection import connectToMySQL
from dojo_flask_app.models.Ninja import Ninja

class Dojo:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.ninjas = []

    @classmethod
    def get_all_dojos( cls ):
        query = "SELECT * FROM dojos"
        results = connectToMySQL( "dojo_ninjas" ).query_db( query )

        dojos = []
        for element in results:
            dojos.append( Dojo( element['id'], element['name'], element['created_at'], element['updated_at']) )
        return dojos

    @classmethod
    def add_dojo( cls, data ):
        query= "INSERT INTO dojos(name) VALUES ( %(name)s );"
        result = connectToMySQL('dojo_ninjas').query_db( query, data )
        return result

    @classmethod
    def get_ninjas_in_dojo( cls, id ):
        query = "SELECT* FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(self.id)s;"
        results = connectToMySQL('dojo_ninjas').query_db(query,id)
        print(results)
        dojo = cls(results[0])
        for row in results:
            
            dojo.ninjas.append( Ninja( row['todo_id'], row['todo'], row['completed'], row['username'] ))
        return dojo
        
