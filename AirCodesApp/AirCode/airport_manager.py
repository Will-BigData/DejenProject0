
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
      

