import psycopg2
from decouple import config

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

class Restaurant:
    def __init__(self, id=None, name=None, location=None, description=None, category=None, total_grade=0, user_id=None):
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.category = category
        self.total_grade = total_grade
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

    def create_restaurant(self, current_user_id):
        if self.user_id != current_user_id:
            print("You cannot create a restaurant for another user.")
            return False

        try:
            conn = self._db_connect()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Restaurants (name, location, description, category, total_grade, user_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.name, self.location, self.description, self.category, self.total_grade, self.user_id)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating restaurant: {e}")
            return False
