import csv
import os
import mysql.connector


class FileManager:
    def __init__(self, host='localhost', user='root', password='your_password', database='airport_management'):
        self.connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='pass',
            database='airportcodes'
        )
        self.cursor = self.connection.cursor(dictionary=True)
        print("Connected to MySQL database")

    # Load data from MySQL database
    def load_from_file(self):
        data = []
        query = "SELECT airport_code AS `Airport Code`, airport_name AS `Airport Name`, city, country FROM airports"
        self.cursor.execute(query)
        data = self.cursor.fetchall()  # Fetch all rows from the airports table
        return data

    # Save data to MySQL database
    def save_to_file(self, data):
        try:
            for airport in data:
                query = query = """
                    INSERT INTO airports (airport_code, airport_name, city, country)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE airport_name = VALUES(airport_name), city = VALUES(city), country = VALUES(country)
                """
                self.cursor.execute(query, (airport['Airport Code'], airport['Airport Name'], airport['city'], airport['country']))
            self.connection.commit()
            print(f"Data successfully saved to MySQL database")
        except Exception as e:
            print(f"Error saving to MySQL database: {e}")

    def close_connection(self):
        self.connection.close()



