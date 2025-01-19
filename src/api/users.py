import psycopg2
import hashlib
from decouple import config

POSTGRES_DB = config("POSTGRES_DB")
POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
POSTGRES_PORT = config("POSTGRES_PORT")


class User:
    def __init__(self, id=None, email=None, name=None, password=None):
        self.id = id
        self.email = email
        self.name = name
        self.password = password

    def _db_connect(self):
        try:
            return psycopg2.connect(
                database=POSTGRES_DB,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                host="localhost",
                port=POSTGRES_PORT,
            )
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def create_user(self):
        try:
            conn = self._db_connect()
            cur = conn.cursor()
            hashed_password = hashlib.md5(self.password.encode()).hexdigest()
            cur.execute(
                "INSERT INTO Users (email, name, password) VALUES (%s, %s, %s)",
                (self.email, self.name, hashed_password),
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def authenticate_user(self):
        try:
            conn = self._db_connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Users WHERE email = %s", (self.email,))
            user = cur.fetchone()
            conn.close()

            if user:
                user_id, email, name, stored_password = user
                hashed_input_password = hashlib.md5(self.password.encode()).hexdigest()

                if hashed_input_password == stored_password:
                    return {"id": user_id, "email": email, "name": name}
            return None
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None
