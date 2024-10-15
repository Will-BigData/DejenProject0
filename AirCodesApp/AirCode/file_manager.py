import csv
import os

class FileManager:
    def __init__(self, file_path='../data/airports.csv'):
        self.file_path = file_path
        #print(f"Using file: {self.file_path}")

    # Load data from the CSV file
    def load_from_file(self):
        data = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        data.append({
                            "Airport Code": row["Airport Code"],
                            "Airport Name": row["Airport Name"],
                            "City": row["City"],  
                            "Country": row["Country"]  
                        })
            except Exception as e:
                print(f"Error reading CSV file: {e}")
        else:
            print(f"File {self.file_path} not found. Starting with an empty list.")
        return data

    def save_to_file(self, new_data):
        try:
            # Overwrite the CSV file with the updated data
            with open(self.file_path, mode='w', newline='') as file:
                fieldnames = ["Airport Code", "Airport Name", "City", "Country"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_data)
                #print(f"Data successfully saved to: {self.file_path}")
            
        except Exception as e:
            print(f"Error saving to CSV file: {e}")


    def close_connection(self):
        print("No connection to close (working with CSV files)")
