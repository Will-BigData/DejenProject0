import csv
import os

class FileManager:
    def __init__(self, file_path='../data/airports.csv'):
        self.file_path = file_path
        print(f"Using file: {self.file_path}")

    # Load data from the CSV file
    def load_from_file(self):
        data = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Read existing data and load into memory
                        data.append({
                            "Airport Code": row["Airport Code"],
                            "Airport Name": row["Airport Name"],
                            "City": row["City"],
                            "Country": row["Country"]
                        })
                #print(f"Loaded data from: {self.file_path}")
            except Exception as e:
                print(f"Error reading CSV file: {e}")
        else:
            print(f"File {self.file_path} not found. Starting with an empty list.")
        return data

    # Save data to a CSV file (append new data while preserving old data)
    def save_to_file(self, data):
        existing_data = self.load_from_file()  # Load existing data first

        # Merge new data with existing data
        all_data = existing_data + data

        try:
            with open(self.file_path, mode='w', newline='') as file:
                fieldnames = ["Airport Code", "Airport Name", "city", "country"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)  # Write the entire list of airports (existing + new)
                print(f"Data successfully saved to: {self.file_path}")
        except Exception as e:
            print(f"Error saving to CSV file: {e}")

    def close_connection(self):
        print("No connection to close (working with CSV files)")
