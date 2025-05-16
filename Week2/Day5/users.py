import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'hicham'
PASSWORD = 'root'
DATABASE = 'userManagement'

class users():
    def __init__(self):
        try:
            self.connect = psycopg2.connect(
                    host=HOSTNAME, 
                    user=USERNAME, 
                    password=PASSWORD, 
                    dbname=DATABASE)
            self.cursor = self.connect.cursor()
            # print("Connected to <userManagement> Database successfully")

        except Exception as e:
            print("Error: ", e)
    
    @classmethod
    def read_all(cls):
        self = cls()
        query = '''
                    SELECT * FROM users;
                '''
        self.cursor.execute(query)
        self.connect.commit()
        result = self.cursor.fetchall()
        # print(result)
        return (result)
    
    @classmethod
    def read(cls, user_id):
        self = cls()

        cls.check("id", user_id)

        query = '''
                    SELECT * FROM users where user_id = %s;
                '''
        self.cursor.execute(query, (user_id,))
        self.connect.commit()
        result = self.cursor.fetchall()
        if not result:
            return None
        return result

    @classmethod
    def create(cls, first_name, last_name):
        self = cls()

        cls.check("name", first_name, last_name)

        query = '''
                    INSERT INTO users(first_name, last_name)
                    VALUES (%s, %s)
                '''
        self.cursor.execute(query, (first_name, last_name))
        self.connect.commit()
        return f"User {first_name} {last_name} has been created successfully"

    @classmethod
    def delete(cls, user_id):
        self = cls()

        cls.check("id", user_id)

        query = '''
                    DELETE FROM users WHERE user_id = %s;
                '''
        self.cursor.execute(query, (user_id,))
        self.connect.commit()

        if self.cursor.rowcount == 0:
            return None
        else:
            return f"User userid:‘{user_id}‘ has been deleted successfully."
    
    @classmethod
    def update(cls, user_id, first_name, last_name):
        self = cls()

        cls.check("update", first_name, last_name, user_id)

        query = '''
                    UPDATE users
                    SET first_name = %s, last_name = %s
                    WHERE user_id = %s;
                '''
        
        self.cursor.execute(query, (first_name, last_name, user_id))
        self.connect.commit()
        if self.cursor.rowcount == 0:
            return None
        else:
            return f"User userid:‘{user_id}‘ has been updated successfully"
    



    # Checker made by AI --------------------------------------------------
    @staticmethod
    def check(param_type, *args):
        """
        Validates input parameters based on parameter type
        
        param_type: string indicating which operation to validate for
        args: parameters to validate
        
        Raises UserValidationError if validation fails
        """
        if param_type == "id":
            # Check if ID is valid (integer and positive)
            if len(args) != 1:
                raise Exception("ID validation requires exactly one parameter")
            
            id_value = args[0]
            if not isinstance(id_value, int) and not (isinstance(id_value, str) and id_value.isdigit()):
                raise Exception(f"Invalid ID: {id_value}. ID must be an integer or a string containing only digits")
            
            # Convert string to int if it's a string
            if isinstance(id_value, str):
                id_value = int(id_value)
                
            if id_value <= 0:
                raise Exception(f"Invalid ID: {id_value}. ID must be positive")
            
        elif param_type == "name":
            # Check if names are valid (non-empty strings)
            if len(args) != 2:
                raise Exception("Name validation requires exactly two parameters (first_name, last_name)")
                
            first_name, last_name = args
            
            if not isinstance(first_name, str) or not first_name.strip():
                raise Exception(f"Invalid first_name: {first_name}. First name must be a non-empty string")
                
            if not isinstance(last_name, str) or not last_name.strip():
                raise Exception(f"Invalid last_name: {last_name}. Last name must be a non-empty string")
            
        elif param_type == "update":
            # Check if all update parameters are valid
            if len(args) != 3:
                raise Exception("Update validation requires exactly three parameters (first_name, last_name, id)")
                
            first_name, last_name, id_value = args
            
            # Validate names and ID (will raise exceptions if invalid)
            try:
                users.check("name", first_name, last_name)
                users.check("id", id_value)
            except Exception as e:
                raise e
            
        else:
            raise Exception(f"Unknown parameter type: {param_type}")



if __name__ == "__main__":
    # user1 = users()
    # print(users.read())
    # print(users.update("Hmad", "Smailli", 2))
    # print(users.read('10'))
    # print(users.delete(2))
    try:
        # users.create('Imad', 'Dabligi')
        # users.create('Hamza', 'Idrissi')
        # users.create('Soad', 'Dbaba')
        # users.create('Halima', 'Idrissi')
        # users.create('Yassin', 'Faill')
        # users.create('Ypussef', 'Hrimat')
        # users.create('Dokali', 'Yajour')
        # print(users.update("Hmad", "Smailli", 4))

        # print(users.read('1'))
        print(users.read_all())
    
    except Exception as e:
        print("error: ", e)

    

