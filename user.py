from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users').query_db(query, data)

# READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users";
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

# UPDATE
    @classmethod
    def edit(cls, data):            # Should be get_one_user() but it's too far along to change now!
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)
    
# DELETE
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)