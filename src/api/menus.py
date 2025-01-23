import psycopg2
from decouple import config

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

class Menu:
    def __init__(self, id=None, name=None, description=None, menu_photo=None, restaurant_id=None, user_id=None):
        self.id = id
        self.name = name
        self.description = description
        self.menu_photo = menu_photo
        self.restaurant_id = restaurant_id
        self.user_id = user_id

    def _db_connect(self):
        try:
            return psycopg2.connect(
                database=POSTGRES_DB,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                host="localhost",
                port=POSTGRES_PORT
            )
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def fetch_all_menus(self):
        try:
            conn = self._db_connect()
            cur = conn.cursor()
            
            cur.execute("""
                SELECT m.id, m.name, m.description, m.menu_photo, m.restaurant_id, r.name AS restaurant_name, m.user_id
                FROM "Menus" m
                JOIN "Restaurants" r ON m.restaurant_id = r.id
            """)
            menus = cur.fetchall()
            
            menu_list = []
            for row in menus:
                menu_list.append({
                    "id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "menu_photo": row[3],
                    "restaurant_id": row[4],  # Incluindo o campo restaurant_id
                    "restaurant_name": row[5],
                    "user_id": row[6]
                })
            
            conn.close()
            return menu_list
        except Exception as e:
            print(f"Error fetching menus: {e}")
            return []

        
    def create_menu(self):
        if not all([self.name, self.description, self.restaurant_id, self.user_id]):
            print("Missing required fields for creating a menu.")
            return False

        try:
            conn = self._db_connect()
            cur = conn.cursor()
            
            cur.execute(
                """
                INSERT INTO "Menus" (name, description, menu_photo, restaurant_id, user_id)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.name, self.description, self.menu_photo, self.restaurant_id, self.user_id)
            )
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating menu: {e}")
            return False

    def delete_menu(self, menu_id, current_user_id):
        try:
            conn = self._db_connect()
            cur = conn.cursor()

            cur.execute('SELECT user_id FROM "Menus" WHERE id = %s', (menu_id,))
            result = cur.fetchone()

            if not result:
                print(f"Menu not found.")
                conn.close()
                return False

            user_id = result[0]
            if user_id != current_user_id:
                print("You do not have permission to delete this menu.")
                conn.close()
                return False
            
            cur.execute('DELETE FROM "Menus" WHERE id = %s', (menu_id,))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error deleting menu: {e}")
            return False
