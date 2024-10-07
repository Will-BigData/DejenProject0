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
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice")
            if choice == "1":
                self.add_airport()
            elif choice == "2":
                self.view_airports()
            elif choice == "3":
                self.search_airport_by_code()
            elif choice == "4":
                self.search_airport_by_name()
            elif choice == "5":
                self.save_and_exit()
            else:
                print("Invalid choice")
    def add_airport(self):
        code = input("Enter the airport code: ").strip().upper()
        name = input("Enter the airport name: ").strip()

        if code == "" and name == "":
            print("Airport code and name cannot be empty")
        else:
            result = self.airport_manager.add_airport(code, name)
            if result:
                print("Airport added successfully")
                self.file_manager.save_to_file(self.airport_manager.airports)
            else:
                print("Airport already exists")

if __name__ == "__main__":
    app = AirportApp()
    app.display_menu()
   
