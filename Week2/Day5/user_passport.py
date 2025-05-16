import psycopg2
from datetime import datetime, date
# from config import HOSTNAME, USERNAME, PASSWORD, DATABASE

HOSTNAME = 'localhost'
USERNAME = 'hicham'
PASSWORD = 'root'
DATABASE = 'userManagement'

class user_passport:
    def __init__(self):
        try:
            self.connect = psycopg2.connect(
                host=HOSTNAME, 
                user=USERNAME, 
                password=PASSWORD, 
                dbname=DATABASE)
            self.cursor = self.connect.cursor()
        except Exception as e:
            print("Error:", e)

    @classmethod
    def create(cls, user_id, nationality, expire_date):
        self = cls()
        cls.check("create", user_id, nationality, expire_date)

        query = '''
            INSERT INTO user_passport (user_id, nationality, expire_date)
            VALUES (%s, %s, %s);
        '''
        self.cursor.execute(query, (user_id, nationality, expire_date))
        self.connect.commit()
        return f"Passport created successfully for user_id {user_id}"

    @classmethod
    def read_all(cls):
        self = cls()
        query = ''' 
                    SELECT up.passport_id, up.user_id, u.first_name, u.last_name, up.nationality, up.expire_date 
                    FROM user_passport up
                    INNER JOIN users u ON up.user_id = u.user_id;
                '''
        self.cursor.execute(query)
        self.connect.commit()
        return self.cursor.fetchall()

    @classmethod
    def read(cls, user_id):
        self = cls()
        cls.check("id", user_id)

        query = '''
            SELECT up.passport_id, up.user_id, u.first_name, u.last_name, up.nationality, up.expire_date
            FROM user_passport up
            INNER JOIN users u ON up.user_id = u.user_id
            WHERE up.user_id = %s;
        '''
        self.cursor.execute(query, (user_id,))
        self.connect.commit()
        result = self.cursor.fetchall()
        return result if result else None

    @classmethod
    def delete(cls, user_id):
        self = cls()
        cls.check("id", user_id)

        query = 'DELETE FROM user_passport WHERE user_id = %s;'
        self.cursor.execute(query, (user_id,))
        self.connect.commit()
        if self.cursor.rowcount == 0:
            return None
        return f"Passport for user_id {user_id} has been deleted successfully."

    @staticmethod
    def check(param_type, *args):
        if param_type == "id":
            if len(args) != 1:
                raise Exception("ID validation requires exactly one parameter")
            id_value = args[0]
            if not isinstance(id_value, int) and not (isinstance(id_value, str) and id_value.isdigit()):
                raise Exception("Invalid user_id. Must be integer or digit string")
            if int(id_value) <= 0:
                raise Exception("User ID must be a positive number")

        elif param_type == "create":
            if len(args) != 3:
                raise Exception("Create validation requires user_id, nationality, and expire_date")
            user_id, nationality, expire_date = args

            # Validate user_id using existing logic
            user_passport.check("id", user_id)

            # Validate nationality
            if not isinstance(nationality, str) or not nationality.strip():
                raise Exception("Nationality must be a non-empty string")

            # Validate expire_date: either string or datetime.date
            if isinstance(expire_date, str):
                try:
                    datetime.strptime(expire_date, "%Y-%m-%d")
                except ValueError:
                    raise Exception("Expire date must be in YYYY-MM-DD format")
            elif not isinstance(expire_date, date):
                raise Exception("Expire date must be a string in YYYY-MM-DD format or a date object")

        else:
            raise Exception(f"Unknown parameter type: {param_type}")
