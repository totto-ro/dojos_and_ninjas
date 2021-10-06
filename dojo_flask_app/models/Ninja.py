from dojo_flask_app.config.MySQLConnection import connectToMySQL

class Ninja:
    def __init__(self, id, first_name, last_name, age, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age=age
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def add_ninja( cls, data ):
        query= "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL('dojo_ninjas').query_db( query, data )
        return result

    
