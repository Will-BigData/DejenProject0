from file_manager import FileManager
from airport_manager import AirportManager


class AirportApp:
    def __init__(self):
        self.airports = []
    def display_menu(self):
        print(" Welcome to Airport Codes Management System Application")
        print("1. Add Airport Code")
        print("2. View All Airport Codes")
        print("3. Search Airport by Code")
        print("4. Search Airport by Name")
        print("5. Save and Exit")

if __name__ == "__main__":
    app = AirportApp()
    app.display_menu()
   
