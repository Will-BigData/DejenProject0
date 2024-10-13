class AirportManager:
    def __init__(self, airports=None):
        # Initialize with existing airports or start with an empty list
        self.airports = airports if airports else []

    def airport_exists(self, code):
        return any(airport["Airport Code"] == code for airport in self.airports)

    def add_airport(self, code, name, city, country):
        if self.airport_exists(code):
            return False, f"Airport code '{code}' already exists."
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
        return self.airports

    def view_airport_by_code(self, code):
        airport = next(
            (airport for airport in self.airports if airport["Airport Code"] == code), None)
        return airport if airport else f"No airport found with code '{code}'."

    def search_airports_by_name(self, name):
        matching_airports = [airport for airport in self.airports if name.lower(
        ) in airport["Airport Name"].lower()]
        return matching_airports if matching_airports else f"No airports found matching '{name}'."

    def get_airports(self):
        return self.airports

   
    def update_airport(self, old_code, new_code, new_name, new_city, new_country):
        for airport in self.airports:
            if airport["Airport Code"] == old_code:
                airport["Airport Code"] = new_code
                airport["Airport Name"] = new_name
                airport["City"] = new_city
                airport["Country"] = new_country
                return True, f"Airport updated successfully: Code: {new_code}, Name: {new_name}, City: {new_city}, Country: {new_country}"
        return False, f"Airport with code '{old_code}' not found."


    def remove_airport_by_code(self, code):
        """Removes an airport from the list by its code."""
        for idx, airport in enumerate(self.airports):
            if airport["Airport Code"] == code:
                # Remove the airport from the list
                del self.airports[idx]
                return True, f"Airport with code '{code}' has been removed."
        return False, f"No airport found with code '{code}'."
