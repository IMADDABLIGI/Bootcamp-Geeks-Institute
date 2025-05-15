import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'hicham'
PASSWORD = 'root'
DATABASE = 'restaurant'

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def run_query(self, query, values=None, is_result=False):
        result = ''
        try:
            connect = psycopg2.connect(
                host=HOSTNAME, 
                user=USERNAME, 
                password=PASSWORD, 
                dbname=DATABASE)
        except Exception as e:
            print(f"Error: {e}")
        
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        if is_result:
            result = cursor.fetchall()
        connect.close()
        return result
        

    def save(self):
        save_item = f'''
                    INSERT INTO menu_items(item_name, item_price)
                    VALUES (%s, %s);
                    '''
        self.run_query(save_item, (self.name, self.price))

    def delete(self):
        delete_item = f"DELETE FROM menu_items  WHERE item_name = '{self.name}';"
        self.run_query(delete_item)
    
    def update(self, name, price):
        pass


if __name__ == "__main__":
    create_table_qr = f'''
                CREATE TABLE Menu_Items(
                    item_id SERIAL PRIMARY KEY,
                    item_name VARCHAR(30) NOT NULL,
                    item_price SMALLINT DEFAULT 0
                )
                '''
    # MenuItem.run_query(create_table_qr)
    danon = MenuItem("Danon", 5)
    danon.delete()


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)