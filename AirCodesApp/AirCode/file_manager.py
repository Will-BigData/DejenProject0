import csv
import os

class FileManager:
    def __init__(self, file_path='../data/airports.csv'):
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
    


    #save data to file
    def save_to_file(self, data):
        with open(self.file_path, mode='w', newLine='') as file:
            writer  = csv.DictWriter(file, fieldnames=["Airport Code", "Airport Name"])
            writer.writeheader()
            writer.writerows(data)
        print("Data saved successfully")
