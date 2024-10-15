import mysql.connector
from file_manager import FileManager

class AirportManager:
    def __init__(self, file_manager):
        # Initialize with a file manager that connects to MySQL
        self.file_manager = file_manager
        self.airports = self.file_manager.load_from_file()  # Load airports from MySQL database

    def airport_exists(self, code):
        # Check if an airport with the given code exists in the database
        query = "SELECT airport_code FROM airports WHERE airport_code = %s"
        self.file_manager.cursor.execute(query, (code,))
        result = self.file_manager.cursor.fetchone()
        return result is not None

    def add_airport(self, code, name, city, country):
        if self.airport_exists(code):
            return False, f"Airport code '{code}' already exists."

        query = "INSERT INTO airports (airport_code, airport_name, city, country) VALUES (%s, %s, %s, %s)"
        try:
            self.file_manager.cursor.execute(query, (code, name, city, country))
            self.file_manager.connection.commit()
            return True, f"Airport '{name}' with code '{code}' added successfully."
        except Exception as e:
            return False, f"Error adding airport: {e}"

    def view_airports(self):
        query = "SELECT airport_code AS `Airport Code`, airport_name AS `Airport Name`, city AS `City`, country AS `Country` FROM airports"
        try:
            self.file_manager.cursor.execute(query)
            return self.file_manager.cursor.fetchall()
        except Exception as e:
            return f"Error retrieving airports: {e}"

    def view_airport_by_code(self, code):
        query = "SELECT airport_code AS `Airport Code`, airport_name AS `Airport Name`, city AS `City`, country AS `Country` FROM airports WHERE airport_code = %s"
        try:
            self.file_manager.cursor.execute(query, (code,))
            result = self.file_manager.cursor.fetchone()
            return result if result else f"No airport found with code '{code}'."
        except Exception as e:
            return f"Error retrieving airport by code: {e}"

    def search_airports_by_name(self, name):
        query = "SELECT airport_code AS `Airport Code`, airport_name AS `Airport Name`, city AS `City`, country AS `Country` FROM airports WHERE airport_name LIKE %s"
        try:
            self.file_manager.cursor.execute(query, (f"%{name}%",))
            result = self.file_manager.cursor.fetchall()
            return result if result else f"No airports found matching '{name}'."
        except Exception as e:
            return f"Error searching airports by name: {e}"

    def get_airports(self):
        # Return all airports from MySQL
        return self.view_airports()

    def update_airport(self, old_code, new_code, new_name, new_city, new_country):
        query = "UPDATE airports SET airport_code = %s, airport_name = %s, city = %s, country = %s WHERE airport_code = %s"
        try:
            self.file_manager.cursor.execute(query, (new_code, new_name, new_city, new_country, old_code))
            self.file_manager.connection.commit()
            if self.file_manager.cursor.rowcount > 0:
                return True, f"Airport updated successfully: Code: {new_code}, Name: {new_name}, City: {new_city}, Country: {new_country}"
            else:
                return False, f"Airport with code '{old_code}' not found."
        except Exception as e:
            return False, f"Error updating airport: {e}"

    def remove_airport_by_code(self, code):
        confirmation = input(f"Are you sure you want to delete the airport with code '{code}'? (y/n): ").strip().lower()
        
        if confirmation != 'y':
            return False, "Deletion cancelled by user."

        query = "DELETE FROM airports WHERE airport_code = %s"
        try:
            self.file_manager.cursor.execute(query, (code,))
            self.file_manager.connection.commit()
            if self.file_manager.cursor.rowcount > 0:
                return True, f"Airport with code '{code}' has been removed."
            else:
                return False, f"No airport found with code '{code}'."
        except Exception as e:
            return False, f"Error deleting airport: {e}"
