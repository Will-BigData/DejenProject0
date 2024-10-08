
class AirportManager:
    def __init__(self, airports=None):
        self.airport = airports 
        if self.airport is None:
            self.airport = []
   
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
    
    def view_airport_by_code(self, code):
        for airport in self.airports:
            if airport["Airport Code"] == code:
                return airport
        return f"No airport found with code {code}"



