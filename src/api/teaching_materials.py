from decouple import config
from globals import logged_user
import psycopg2

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')


class TeachingMaterial:
    def __init__(
            self, 
            id = None, 
            description = None, 
            category = None, 
            date_acquisition = None, 
            serie_number = None,
            conservation_status = None, 
            physical_location = None, 
            material_cover_url = None, 
            status = None,
        ):
        self.id = id
        self.description = description
        self.category = category
        self.date_acquisition = date_acquisition
        self.serie_number = serie_number
        self.conservation_status = conservation_status
        self.physical_location = physical_location
        self.material_cover_url = material_cover_url
        self.status = status

    def _bd_connect(self):
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

    def create_teaching_material(self):
        with open('src/globals.py', 'r') as file:
            exec(file.read())
    
        if logged_user['role'] is None:
            print('You must be logged in to create a teaching material')
            return False
        
        if logged_user["role"] != 'ADMIN':
            print('You do not have permission to create a teaching material')
            return False
    
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Teaching_materials (description, category, date_acquisition, serie_number, conservation_status, physical_location, material_cover_url, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.description, 
                    self.category, 
                    self.date_acquisition, 
                    self.serie_number,
                    self.conservation_status, 
                    self.physical_location, 
                    self.material_cover_url, 
                    self.status
                )
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error inserting teaching material: {e}')
            return False

    def update_teaching_material(self):
        with open('src/globals.py', 'r') as file:
            exec(file.read())
    
        if logged_user['role'] is None:
            print('You must be logged in to update a teaching material')
            return False
        
        if logged_user["role"] != 'ADMIN':
            print('You do not have permission to update a teaching material')
            return False
    
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Teaching_materials SET description = %s, category = %s, date_acquisition = %s, serie_number = %s, conservation_status = %s, physical_location = %s, material_cover_url = %s, status = %s WHERE id = %s",
                (
                    self.description, 
                    self.category, 
                    self.date_acquisition, 
                    self.serie_number, 
                    self.conservation_status, 
                    self.physical_location, 
                    self.material_cover_url, 
                    self.status, 
                    self.id
                )
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error updating teaching material: {e}')
            return False

    def delete_teaching_material(self):
        with open('src/globals.py', 'r') as file:
            exec(file.read())

        if logged_user['role'] is None:
            print('You must be logged in to delete a teaching material')
            return False
        
        if logged_user["role"] != 'ADMIN':
            print('You do not have permission to delete a teaching material')
            return False
    
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Teaching_materials WHERE id = %s",
                (self.id,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error deleting teaching material: {e}')
            return False

    def get_teaching_materials(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Teaching_materials')
            materials_data = cur.fetchall()
            conn.close()
            
            materials = []
            for material_data in materials_data:
                material = TeachingMaterial(*material_data)
                materials.append(material)

            materials.sort(key=lambda x: x.id)
            
            return materials
        except Exception as e:
            print(f'Error fetching teaching materials: {e}')

    def get_teaching_material_by_id(self):

        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Teaching_materials WHERE id = %s', (self.id,))
            material_data = cur.fetchone()
            conn.close()

            if material_data:
                material = TeachingMaterial(*material_data)
                return material
        
            return material
        except Exception as e:
            print(f'Error fetching teaching material: {e}')

    def get_available_teaching_materials(self):

        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Teaching_materials WHERE status = 'AVAILABLE'")
            available_materials = cur.fetchall()
            conn.close()

            materials = []
            for material_data in available_materials:
                material = TeachingMaterial(*material_data)
                materials.append(material)

            return materials
        except Exception as e:
            print(f'Error fetching available teaching materials: {e}')
