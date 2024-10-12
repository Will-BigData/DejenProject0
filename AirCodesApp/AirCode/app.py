from colorama import Fore, Style, init
from tabulate import tabulate
from file_manager import FileManager
from airport_manager import AirportManager


class AirportApp:
    def __init__(self):
        self.file_manager = FileManager(file_path='../data/airports.csv')
        airports_data = self.file_manager.load_from_file()
        self.airport_manager = AirportManager(airports_data)

    def display_menu(self):
        print('\n')
        print(Fore.CYAN + Style.BRIGHT + f"{'='*45:^90}")
        print(Fore.GREEN + Style.BRIGHT + f"{'  WELCOME TO AIRPORT CODES MANAGEMENT SYSTEM ':^90}")
        print(Fore.CYAN + Style.BRIGHT + f"{'='*45:^90}")
        print(Style.RESET_ALL)

        print(Fore.GREEN + Style.BRIGHT + f"{' Ready to find your airport code? Please choose an option below.':^90}")
        print('\n')

        print("1. Add Airport Code")
        print("2. View All Airport Codes")
        print("3. Search Airport by Code")
        print("4. Search Airport by Name")
        print("5. Save and Exit")
        print('\n')

    def run(self):
        while True:
            self.display_menu()
            choice = input(Fore.CYAN + Style.BRIGHT + "Enter your choice: ")
            while not self.validate_choice(choice, ["1", "2", "3", "4", "5"]):
                print("Invalid choice. Please enter a number from 1 to 5. ")
                choice = input(Fore.CYAN + Style.BRIGHT + "Enter your choice: ")
            if self.validate_choice(choice, ["1", "2", "3", "4", "5"]):
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
                    break
            else:
                print("Invalid choice. Please enter a number from 1 to 5. ")
            choice = input(Fore.CYAN + Style.BRIGHT + "Enter your choice: ")
            

    def add_airport(self):
        code = input("Enter the airport code: ").strip().upper()
        name = input("Enter the airport name: ").strip()
        city = input("Enter the city name: ").strip()
        country = input("Enter the country name: ").strip()
        print('\n')

        if not code or not name:
            print("Airport code and name cannot be empty.")
        else:
            success, message = self.airport_manager.add_airport(code, name, city, country)
            print(message)
            if success:
                # Save to CSV after successfully adding the airport
                self.file_manager.save_to_file(self.airport_manager.get_airports())

    def view_airports(self):
        airports = self.airport_manager.view_airports()
        if isinstance(airports, str):
            print(airports)  # "No airports found" message
        else:
            self.display_table(airports)
            print('\n')
    
    def search_airport_by_code(self):
        code = input("Enter the airport code: ").strip().upper()
        airport = self.airport_manager.view_airport_by_code(code)
        if isinstance(airport, str):
            print(airport)
        else:
            self.display_table([airport])
            print('\n')
            # print(f"Code: {airport['Airport Code']}, Name: {airport['Airport Name']}, City: {airport['city']}, Country: {airport['country']}")

    def search_airport_by_name(self):
        name = input("Enter the airport name to search (partial match allowed): ").strip().lower()
        matching_airports = self.airport_manager.search_airports_by_name(name)
        if isinstance(matching_airports, str):
            print(matching_airports)
        else:
            self.display_table(matching_airports)


        #display airport data using tabulate
    def display_table(self, data):
        table = []
        for idx, airport in enumerate(data):
            table.append([idx + 1, airport['Airport Code'], airport['Airport Name'], airport['City'], airport['Country']])

        headers = ['No.', 'Airport Code', 'Airport Name', 'City', 'Country']
        print(tabulate(table, headers, tablefmt="fancy_grid"))


    def save_and_exit(self):
        self.file_manager.save_to_file(self.airport_manager.get_airports())
        print("Data saved successfully. Exiting...")

    def validate_choice(self, choice, valid_choices):
        return choice in valid_choices


if __name__ == "__main__":
    app = AirportApp()
    app.run()
