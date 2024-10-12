class AirportManager:
    def __init__(self, airports=None):
        self.airports = airports if airports else []

    def airport_exists(self, code):

        for airport in self.airports:
            if airport["Airport Code"] == code:
                return True
        return False
        
    def add_airport(self, code, name, city, country):
        if self.airport_exists(code):
            return False, f"Airport code '{code}' already exists."
        else:
            self.airports.append({
                "Airport Code": code, 
                "Airport Name": name, 
                "City": city,      
                "Country": country
            })
            return True, f"Airport '{name}' with code '{code}' added successfully."

    def view_airports(self):
        if not self.airports:
            return "No airports found."
        else:
            return self.airports

    def view_airport_by_code(self, code):
        for airport in self.airports:
            if airport["Airport Code"] == code:
                return airport
        return f"No airport found with code '{code}'."

    def search_airports_by_name(self, name):
        matching_airports = [airport for airport in self.airports if name.lower() in airport["Airport Name"].lower()]
        return matching_airports if matching_airports else f"No airports found matching '{name}'."

    def get_airports(self):
        return self.airports
