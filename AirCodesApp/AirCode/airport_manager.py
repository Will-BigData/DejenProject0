
class AirportManager:
    def __init__(self, airports=None):
       self.airports = airports if airports else []
   
    def airport_exists(self, code):
        for airport in self.airports:
            if airport["Airport Code"] == code:
                return True
        return False
    
    # add a new airport to the list
    def add_airport(self, code, name):
        if self.airport_exists(code):
            return False, f"Airport with code {code} already exists."
        else:
            self.airports.append({"Airport Code": code, "Airport Name": name})
            return True, f"Airport '{name}' with code '{code}' added successfully"
        
    def view_airports(self):
        if not self.airports:
            print("No airports found")
        else:
            return self.airports
    
    def search_airport_by_code(self, code):
        for airport in self.airports:
            if airport["Airport Code"] == code:
                return airport
        return f"No airport found with code {code}"
    

    def search_airport_by_name(self, name):
        matching_airports = []
        for airport in self.airports:
            if name.lower() in airport["Airport Name"].lower():
                matching_airports.append(airport)
            
        if matching_airports:
            return matching_airports
        else:
            return f"No airport found with name {name}"

    def get_airports(self):
        return self.airports


