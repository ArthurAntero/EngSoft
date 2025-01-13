from decouple import config
import psycopg2

class Database:
  def __init__():
      POSTGRES_DB = config('POSTGRES_DB')
      POSTGRES_USER = config('POSTGRES_USER')
      POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
      POSTGRES_PORT = config('POSTGRES_PORT')
      
      try:
          conn = psycopg2.connect(
              database=POSTGRES_DB,
              user=POSTGRES_USER,
              password=POSTGRES_PASSWORD,
              host="localhost",
              port=POSTGRES_PORT
          )
          return conn
      except Exception as e:
          print(f'Error connecting to the database: {e}')