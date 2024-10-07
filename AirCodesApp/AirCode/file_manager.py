import csv
import os

class FileManager:
    def __init__(self, file_path):
        self.file_path=file_path
        print(f"Using file path: {self.file_path}")

    def load_data(self):
        data = []
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, mode='r', newLine='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        data.append({"Airport Code": row["Airport Code"], "Airport Name": row["Airport Name"]})
            except Exception as e:
                print(f"Error loading data: {e}")
        else:
            print(f"File {self.file_path} not found")
        return data