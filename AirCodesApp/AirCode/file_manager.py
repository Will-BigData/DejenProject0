import csv
import os
import mysql.connector
from dotenv import load_dotenv

class FileManager:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Fetch values from the environment variables
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_NAME')

        # Connect to the MySQL database using the environment variables
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)
        print(f"Connected to MySQL database: {database}")

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



