import psycopg2
from decouple import config

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

class Review:
    def __init__(self, id=None, description=None, grade=None, restaurant_id=None, user_id=None):
        self.id = id
        self.description = description
        self.grade = grade
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

    def create_review(self, current_user_id):
        if self.user_id != current_user_id:
            print("You cannot create a review for another user.")
            return False

        try:
            conn = self._db_connect()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Review (description, grade, restaurant_id, user_id) VALUES (%s, %s, %s, %s)",
                (self.description, self.grade, self.restaurant_id, self.user_id)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating review: {e}")
            return False
