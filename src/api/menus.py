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

    def create_menu(self, current_user_id):
        if self.user_id != current_user_id:
            print("You cannot create a menu for another user's restaurant.")
            return False

        try:
            conn = self._db_connect()
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO "Menus" (name, description, menu_photo, restaurant_id, user_id) VALUES (%s, %s, %s, %s, %s)',
                (self.name, self.description, self.menu_photo, self.restaurant_id, self.user_id)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating menu: {e}")
            return False
